"""Core implementation of the AI Agent."""

import os
from collections.abc import Iterable
from dotenv import load_dotenv
import instructor
from openai import OpenAI
from openai.types.chat import ChatCompletionChunk

from .prompts import SYSTEM_PROMPT

# Load environment variables from .env file
load_dotenv()


class AgentCore:
    """
    The core agent class that handles LLM communication.
    """

    def __init__(self):
        """
        Initializes the AgentCore, loading configuration from the environment.

        Raises:
            ValueError: If required environment variables are not set.
        """
        llm_base_url = os.getenv("LLM_BASE_URL")
        llm_api_key = os.getenv("LLM_API_KEY")
        self.llm_choice = os.getenv("LLM_CHOICE")

        if not all([llm_base_url, llm_api_key, self.llm_choice]):
            raise ValueError(
                "Missing one or more required environment variables: "
                "LLM_BASE_URL, LLM_API_KEY, LLM_CHOICE"
            )

        # Patch the OpenAI client with instructor
        self.client = instructor.patch(OpenAI(base_url=llm_base_url, api_key=llm_api_key))

    def chat(self, user_input: str) -> str:
        """
        Handles a single conversation turn with the LLM.

        Args:
            user_input: The user's message.

        Returns:
            The response content from the LLM.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.llm_choice,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input},
                ],
                stream=False,  # Changed for debugging
            )
            return response.choices[0].message.content
        except Exception as e:
            # Re-raise the exception to be caught by the CLI's error handler
            raise e