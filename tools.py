import os
import requests
import json
from supabase import create_client, Client

def _get_supabase_client() -> Client:
    """
    Initializes and returns a Supabase client.
    """
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        raise ValueError("Supabase URL or Key not found in environment variables.")
    return create_client(url, key)

def web_search(query: str) -> str:
    """
    Performs a web search using the Brave Search API.

    Args:
        query (str): The search query.

    Returns:
        str: A JSON string of the search results.
    """
    api_key = os.getenv("BRAVE_API_KEY")
    if not api_key:
        return json.dumps({"error": "BRAVE_API_KEY not found in environment variables."})

    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": api_key
    }
    params = {
        "q": query
    }
    url = "https://api.search.brave.com/res/v1/web/search"

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return json.dumps(response.json())
    except requests.exceptions.RequestException as e:
        return json.dumps({"error": str(e)})

def list_documents() -> str:
    """
    Lists available documents from the RAG pipeline.

    Returns:
        str: A JSON string of the document list.
    """
    try:
        supabase = _get_supabase_client()
        response = supabase.from_('documents').select('id, metadata->>title as title, metadata->>source as source').execute()
        return json.dumps(response.data)
    except ValueError as e:
        return json.dumps({"error": str(e)})
    except Exception as e:
        return json.dumps({"error": f"Failed to list documents: {e}"})

def get_document_content(document_id: str) -> str:
    """
    Retrieves the content of a specific document.

    Args:
        document_id (str): The ID of the document.

    Returns:
        str: A JSON string of the document content.
    """
    try:
        supabase = _get_supabase_client()
        response = supabase.from_('document_rows').select('content').eq('document_id', document_id).order('row_number').execute()
        content = "\n".join([row['content'] for row in response.data])
        return json.dumps({"document_id": document_id, "content": content})
    except ValueError as e:
        return json.dumps({"error": str(e)})
    except Exception as e:
        return json.dumps({"error": f"Failed to get document content: {e}"})

def execute_read_only_sql(query: str) -> str:
    """
    Executes a read-only SQL query against tabular data in Supabase.
    This function uses a Supabase RPC function for secure execution.

    Args:
        query (str): The read-only SQL query to execute.

    Returns:
        str: A JSON string of the query results.
    """
    try:
        supabase = _get_supabase_client()
        # Assuming a Supabase RPC function named 'execute_read_only_query' exists
        # that takes the query as a parameter and returns the result.
        response = supabase.rpc('execute_read_only_query', {'sql_query': query}).execute()
        return json.dumps(response.data)
    except ValueError as e:
        return json.dumps({"error": str(e)})
    except Exception as e:
        return json.dumps({"error": f"Failed to execute SQL query: {e}"})