import pytest
from unittest.mock import patch, MagicMock
import json
import os

from tools import web_search, list_documents, get_document_content, execute_read_only_sql

@pytest.fixture
def mock_brave_api_key():
    with patch.dict(os.environ, {"BRAVE_API_KEY": "test_api_key"}):
        yield

@pytest.fixture
def mock_brave_response():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"web": [{"title": "Test Result", "url": "http://test.com"}]}
    return mock_response

@pytest.fixture
def mock_supabase_credentials():
    with patch.dict(os.environ, {"SUPABASE_URL": "http://supabase.test", "SUPABASE_KEY": "test_key"}):
        yield

@pytest.fixture
def mock_supabase_client():
    with patch("tools.create_client") as mock_create_client:
        mock_client = MagicMock()
        mock_create_client.return_value = mock_client
        yield mock_client

def test_web_search_success(mock_brave_api_key, mock_brave_response):
    """Test successful web search."""
    with patch("requests.get", return_value=mock_brave_response) as mock_get:
        result = web_search("test query")
        mock_get.assert_called_once_with(
            "https://api.search.brave.com/res/v1/web/search",
            headers={
                "Accept": "application/json",
                "X-Subscription-Token": "test_api_key"
            },
            params={
                "q": "test query"
            }
        )
        assert json.loads(result) == {"web": [{"title": "Test Result", "url": "http://test.com"}]}

def test_web_search_no_api_key():
    """Test web search when API key is missing."""
    with patch.dict(os.environ, {}, clear=True):
        result = web_search("test query")
        assert json.loads(result) == {"error": "BRAVE_API_KEY not found in environment variables."}

def test_web_search_api_error(mock_brave_api_key):
    """Test web search when API returns an error."""
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("API Error")
    with patch("requests.get", return_value=mock_response):
        result = web_search("test query")
        assert "API Error" in json.loads(result)["error"]

def test_web_search_empty_query(mock_brave_api_key, mock_brave_response):
    """Test web search with an empty query."""
    with patch("requests.get", return_value=mock_brave_response) as mock_get:
        result = web_search("")
        mock_get.assert_called_once_with(
            "https://api.search.brave.com/res/v1/web/search",
            headers={
                "Accept": "application/json",
                "X-Subscription-Token": "test_api_key"
            },
            params={
                "q": ""
            }
        )
        assert json.loads(result) == {"web": [{"title": "Test Result", "url": "http://test.com"}]}

def test_list_documents_success(mock_supabase_credentials, mock_supabase_client):
    """Test successful listing of documents."""
    mock_supabase_client.from_.return_value.select.return_value.execute.return_value.data = [
        {"id": "doc1", "title": "Doc 1", "source": "Source A"},
        {"id": "doc2", "title": "Doc 2", "source": "Source B"}
    ]
    result = list_documents()
    assert json.loads(result) == [
        {"id": "doc1", "title": "Doc 1", "source": "Source A"},
        {"id": "doc2", "title": "Doc 2", "source": "Source B"}
    ]

def test_list_documents_no_credentials():
    """Test listing documents when Supabase credentials are missing."""
    with patch.dict(os.environ, {}, clear=True):
        result = list_documents()
        assert json.loads(result) == {"error": "Supabase URL or Key not found in environment variables."}

def test_list_documents_supabase_error(mock_supabase_credentials, mock_supabase_client):
    """Test listing documents when Supabase interaction fails."""
    mock_supabase_client.from_.return_value.select.return_value.execute.side_effect = Exception("Supabase Error")
    result = list_documents()
    assert "Supabase Error" in json.loads(result)["error"]

def test_get_document_content_success(mock_supabase_credentials, mock_supabase_client):
    """Test successful retrieval of document content."""
    mock_supabase_client.from_.return_value.select.return_value.eq.return_value.order.return_value.execute.return_value.data = [
        {"content": "Line 1"},
        {"content": "Line 2"}
    ]
    result = get_document_content("doc1")
    assert json.loads(result) == {"document_id": "doc1", "content": "Line 1\nLine 2"}

def test_get_document_content_no_credentials():
    """Test getting document content when Supabase credentials are missing."""
    with patch.dict(os.environ, {}, clear=True):
        result = get_document_content("doc1")
        assert json.loads(result) == {"error": "Supabase URL or Key not found in environment variables."}

def test_get_document_content_supabase_error(mock_supabase_credentials, mock_supabase_client):
    """Test getting document content when Supabase interaction fails."""
    mock_supabase_client.from_.return_value.select.return_value.eq.return_value.order.return_value.execute.side_effect = Exception("Supabase Content Error")
    result = get_document_content("doc1")
    assert "Supabase Content Error" in json.loads(result)["error"]

def test_execute_read_only_sql_success(mock_supabase_credentials, mock_supabase_client):
    """Test successful execution of a read-only SQL query."""
    mock_supabase_client.rpc.return_value.execute.return_value.data = [{"column": "value"}]
    result = execute_read_only_sql("SELECT * FROM some_table")
    assert json.loads(result) == [{"column": "value"}]

def test_execute_read_only_sql_no_credentials():
    """Test executing SQL query when Supabase credentials are missing."""
    with patch.dict(os.environ, {}, clear=True):
        result = execute_read_only_sql("SELECT * FROM some_table")
        assert json.loads(result) == {"error": "Supabase URL or Key not found in environment variables."}

def test_execute_read_only_sql_supabase_error(mock_supabase_credentials, mock_supabase_client):
    """Test executing SQL query when Supabase interaction fails."""
    mock_supabase_client.rpc.return_value.execute.side_effect = Exception("Supabase SQL Error")
    result = execute_read_only_sql("SELECT * FROM some_table")
    assert "Supabase SQL Error" in json.loads(result)["error"]