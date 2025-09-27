"""
This module handles the memory system for the Dynomous AI Tutor.
"""

from mem0 import Memory
from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

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
        # Initialize Mem0 with Supabase configuration
        self.memory = Memory(
            config={
                "vector_store": {
                    "provider": "supabase",
                    "config": {
                        "url": os.getenv("SUPABASE_URL"),
                        "key": os.getenv("SUPABASE_KEY"),
                    }
                },
                "llm": {
                    "provider": os.getenv("LLM_PROVIDER"),
                    "config": {
                        "api_key": os.getenv("OPENAI_API_KEY"),
                    }
                },
                "embedder": {
                    "provider": os.getenv("EMBEDDING_PROVIDER"),
                    "config": {
                        "api_key": os.getenv("OPENAI_EMBEDDING_API_KEY"),
                    }
                },
                "custom_fact_extraction_prompt": None,
            }
        )

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
