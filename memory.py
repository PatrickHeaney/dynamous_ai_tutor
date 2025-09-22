"""
This module handles the memory system for the Dynomous AI Tutor.
"""

from mem0ai import Mem0
from typing import List, Dict

class MemoryManager:
    """
    Manages the short-term and long-term memory of the agent.
    """
    def __init__(self, user_id: str):
        """
        Initializes the MemoryManager.

        Args:
            user_id (str): The ID of the user.
        """
        self.user_id = user_id
        self.memory = Mem0()

    def add_message(self, role: str, content: str):
        """
        Adds a message to the conversation memory.

        Args:
            role (str): The role of the message sender (e.g., 'user' or 'assistant').
            content (str): The content of the message.
        """
        self.memory.add(content, user_id=self.user_id, role=role)

    def get_history(self) -> List[Dict[str, str]]:
        """
        Retrieves the conversation history.

        Returns:
            A list of messages, where each message is a dictionary with 'role' and 'content'.
        """
        history = self.memory.get_all(user_id=self.user_id)
        return [{ "role": message["role"], "content": message["content"] } for message in history]

    def search(self, query: str, limit: int = 5) -> List[Dict[str, str]]:
        """
        Searches for relevant memories.

        Args:
            query (str): The query to search for.
            limit (int): The maximum number of memories to return.

        Returns:
            A list of relevant memories.
        """
        return self.memory.search(query, user_id=self.user_id, limit=limit)
