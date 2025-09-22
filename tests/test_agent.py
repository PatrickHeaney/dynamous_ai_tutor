"""
Unit tests for the Dynomous AI agent.
"""
import unittest
from unittest.mock import patch, MagicMock
import os
import sys
from pathlib import Path

# Add project root to sys.path for module discovery
path_to_project_root = Path(__file__).parent.parent
sys.path.insert(0, str(path_to_project_root))

# Set dummy environment variables for testing
os.environ["LLM_PROVIDER"] = "openai"
os.environ["LLM_API_KEY"] = "test_api_key"

from prompts import SYSTEM_PROMPT
from memory import MemoryManager
from agent import DynomousAgent

class TestDynomousAgent(unittest.TestCase):
    """
    Tests for the DynomousAgent class.
    """

    @patch('agent.MemoryManager')
    @patch('agent.Agent')
    @patch('agent.OpenAI')
    def test_initialization(self, mock_openai, mock_agent, mock_memory_manager):
        """
        Test that the agent initializes correctly.
        """
        # Arrange
        mock_llm_instance = MagicMock()
        mock_openai.return_value = mock_llm_instance
        mock_agent_instance = MagicMock()
        mock_agent.return_value = mock_agent_instance
        mock_memory_instance = MagicMock()
        mock_memory_manager.return_value = mock_memory_instance

        # Act
        agent_instance = DynomousAgent(user_id="test_user")

        # Assert
        mock_openai.assert_called_once_with(api_key="test_api_key", base_url=None)
        mock_agent.assert_called_once_with(llm=mock_llm_instance, system_prompt=SYSTEM_PROMPT)
        mock_memory_manager.assert_called_once_with(user_id="test_user")
        self.assertEqual(agent_instance.llm, mock_llm_instance)
        self.assertEqual(agent_instance.agent, mock_agent_instance)
        self.assertEqual(agent_instance.memory, mock_memory_instance)

    @patch('agent.OpenAI')
    def test_initialization_no_api_key(self, mock_openai):
        """
        Test that initialization fails if the API key is missing.
        """
        # Arrange
        original_api_key = os.environ.pop("LLM_API_KEY", None)

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            DynomousAgent()
        
        self.assertTrue("LLM_API_KEY is not set" in str(context.exception))

        # Restore the environment variable
        if original_api_key is not None:
            os.environ["LLM_API_KEY"] = original_api_key

    @patch('agent.MemoryManager')
    @patch('agent.Agent')
    @patch('agent.OpenAI')
    def test_invoke(self, mock_openai, mock_agent, mock_memory_manager):
        """
        Test the invoke method and conversation history.
        """
        # Arrange
        mock_llm_instance = MagicMock()
        mock_openai.return_value = mock_llm_instance
        mock_agent_instance = MagicMock()
        mock_agent_instance.run.return_value = "Test response"
        mock_agent.return_value = mock_agent_instance
        
        mock_memory_instance = MagicMock()
        mock_memory_instance.get_history.return_value = []
        mock_memory_instance.search.return_value = []
        mock_memory_manager.return_value = mock_memory_instance

        agent_instance = DynomousAgent(user_id="test_user")
        query = "Test query"

        # Act
        response = agent_instance.invoke(query)

        # Assert
        self.assertEqual(response, "Test response")
        mock_memory_instance.add_message.assert_any_call(role="user", content=query)
        mock_memory_instance.add_message.assert_any_call(role="assistant", content="Test response")
        mock_memory_instance.get_history.assert_called_once()
        mock_memory_instance.search.assert_called_once_with(query)
        enriched_query = f"Relevant context:\n\n\nUser query: {query}"
        mock_agent_instance.run.assert_called_once_with(input=[{'role': 'user', 'content': enriched_query}])
