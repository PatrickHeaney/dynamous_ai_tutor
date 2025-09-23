"""
Unit tests for the memory manager.
"""
import unittest
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

# Add project root to sys.path for module discovery
path_to_project_root = Path(__file__).parent.parent
sys.path.insert(0, str(path_to_project_root))

from memory import MemoryManager

class TestMemoryManager(unittest.TestCase):
    """
    Tests for the MemoryManager class.
    """

    @patch('memory.Memory')
    def test_add_message(self, mock_mem0):
        """
        Test that a message is added to the memory.
        """
        # Arrange
        mock_mem0_instance = MagicMock()
        mock_mem0.return_value = mock_mem0_instance
        memory_manager = MemoryManager(user_id="test_user")

        # Act
        memory_manager.add_message(role="user", content="Hello")

        # Assert
        mock_mem0_instance.add.assert_called_once_with("Hello", user_id="test_user", role="user")

    @patch('memory.Memory')
    def test_get_history(self, mock_mem0):
        """
        Test that the conversation history is retrieved correctly.
        """
        # Arrange
        mock_mem0_instance = MagicMock()
        mock_mem0_instance.get_all.return_value = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
        mock_mem0.return_value = mock_mem0_instance
        memory_manager = MemoryManager(user_id="test_user")

        # Act
        history = memory_manager.get_history()

        # Assert
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0], {"role": "user", "content": "Hello"})
        self.assertEqual(history[1], {"role": "assistant", "content": "Hi there!"})
        mock_mem0_instance.get_all.assert_called_once_with(user_id="test_user")

    @patch('memory.Memory')
    def test_search(self, mock_mem0):
        """
        Test that the memory search functionality works.
        """
        # Arrange
        mock_mem0_instance = MagicMock()
        mock_mem0_instance.search.return_value = [{"content": "Test memory"}]
        mock_mem0.return_value = mock_mem0_instance
        memory_manager = MemoryManager(user_id="test_user")

        # Act
        results = memory_manager.search(query="test query", limit=1)

        # Assert
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], {"content": "Test memory"})
        mock_mem0_instance.search.assert_called_once_with("test query", user_id="test_user", limit=1)

if __name__ == '__main__':
    unittest.main()
