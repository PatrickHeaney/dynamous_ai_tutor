"""Tests for the AgentCore."""

import os
import pytest
from unittest.mock import MagicMock, patch

# Set dummy environment variables before importing the agent module
os.environ["LLM_BASE_URL"] = "http://dummy-url"
os.environ["LLM_API_KEY"] = "dummy-key"
os.environ["LLM_CHOICE"] = "dummy-model"

from src.agent import AgentCore


@pytest.fixture(autouse=True)
def clear_env_vars():
    """Fixture to clear dummy env vars after each test."""
    yield
    for var in ["LLM_BASE_URL", "LLM_API_KEY", "LLM_CHOICE"]:
        if var in os.environ:
            del os.environ[var]


def test_agent_initialization_success(monkeypatch):
    """Test that AgentCore initializes correctly with environment variables."""
    monkeypatch.setenv("LLM_BASE_URL", "http://fake-url.com")
    monkeypatch.setenv("LLM_API_KEY", "fake-key")
    monkeypatch.setenv("LLM_CHOICE", "fake-model")

    agent = AgentCore()
    assert agent.client is not None
    assert agent.llm_choice == "fake-model"
    assert str(agent.client.base_url) == "http://fake-url.com"


def test_agent_initialization_failure():
    """Test that AgentCore raises ValueError if env vars are missing."""
    with pytest.raises(
        ValueError, match="Missing one or more required environment variables"
    ):
        AgentCore()


@patch("src.agent.instructor.patch")
def test_agent_chat_mocked_response(mock_instructor_patch, monkeypatch):
    """Test the chat loop with a mocked LLM response."""
    monkeypatch.setenv("LLM_BASE_URL", "http://fake-url.com")
    monkeypatch.setenv("LLM_API_KEY", "fake-key")
    monkeypatch.setenv("LLM_CHOICE", "fake-model")

    # 1. Mock the stream response
    mock_delta = MagicMock()
    mock_delta.content = "Hello"
    mock_choice = MagicMock()
    mock_choice.delta = mock_delta
    mock_chunk = MagicMock()
    mock_chunk.choices = [mock_choice]
    mock_stream_iterable = [mock_chunk]

    # 2. Configure the mock client
    mock_patched_client = MagicMock()
    mock_patched_client.chat.completions.create.return_value = mock_stream_iterable
    mock_instructor_patch.return_value = mock_patched_client

    # 3. Run the test
    agent = AgentCore()
    response_stream = agent.chat("Hi")

    # 4. Verify the response
    response_content = ""
    for chunk in response_stream:
        response_content += chunk.choices[0].delta.content

    assert response_content == "Hello"
    mock_patched_client.chat.completions.create.assert_called_once_with(
        model="fake-model",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hi"},
        ],
        stream=True,
    )