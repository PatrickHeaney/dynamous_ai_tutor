"""
Unit tests for the Dynomous AI agent.
"""
import unittest
from unittest.mock import patch, MagicMock
import os

# Set dummy environment variables for testing
os.environ["LLM_PROVIDER"] = "openai"
os.environ["LLM_API_KEY"] = "test_api_key"

from agent import DynomousAgent
from prompts import SYSTEM_PROMPT

class TestDynomousAgent(unittest.TestCase):
    """
    Tests for the DynomousAgent class.
    """

    @patch('agent.Agent')
    @patch('agent.OpenAI')
    def test_initialization(self, mock_openai, mock_pydantic_ai):
        """
        Test that the agent initializes correctly.
        """
        # Arrange
        mock_llm_instance = MagicMock()
        mock_openai.return_value = mock_llm_instance
        mock_agent_instance = MagicMock()
        mock_pydantic_ai.return_value = mock_agent_instance

        # Act
        agent_instance = DynomousAgent()

        # Assert
        mock_openai.assert_called_once_with(api_key="test_api_key", base_url=None)
        mock_pydantic_ai.assert_called_once_with(llm=mock_llm_instance, system_prompt=SYSTEM_PROMPT)
        self.assertEqual(agent_instance.llm, mock_llm_instance)
        self.assertEqual(agent_instance.agent, mock_agent_instance)

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

    @patch('agent.Agent')
    @patch('agent.OpenAI')
    def test_invoke(self, mock_openai, mock_pydantic_ai):
        """
        Test the invoke method and conversation history.
        """
        # Arrange
        mock_llm_instance = MagicMock()
        mock_openai.return_value = mock_llm_instance
        mock_agent_instance = MagicMock()
        mock_agent_instance.run.return_value = "Test response"
        mock_pydantic_ai.return_value = mock_agent_instance

        agent_instance = DynomousAgent()
        query = "Test query"

        # Act
        response = agent_instance.invoke(query)

        # Assert
        self.assertEqual(response, "Test response")
        self.assertEqual(len(agent_instance.conversation_history), 2)
        self.assertEqual(agent_instance.conversation_history[0], {"role": "user", "content": query})
        self.assertEqual(agent_instance.conversation_history[1], {"role": "assistant", "content": "Test response"})
        mock_agent_instance.run.assert_called_once_with(input=[{"role": "user", "content": query}])

if __name__ == '__main__':
    unittest.main()
