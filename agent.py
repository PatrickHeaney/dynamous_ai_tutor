"""
This module defines the core AI agent for the Dynomous AI Tutor.
"""
import os
from pydantic_ai import Agent
from openai import OpenAI
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT

# Load environment variables from .env file
load_dotenv()

class DynomousAgent:
    """
    The main class for the Dynomous AI Tutor agent.
    """
    def __init__(self):
        """
        Initializes the DynomousAgent.
        """
        self.llm = self._initialize_llm()
        self.conversation_history = []
        self.agent = self._create_agent()

    def _initialize_llm(self):
        """
        Initializes the language model based on environment variables.

        Returns:
            An instance of the language model client.
        """
        llm_provider = os.getenv("LLM_PROVIDER", "openai").lower()

        if llm_provider == "openai":
            api_key = os.getenv("LLM_API_KEY")
            base_url = os.getenv("LLM_BASE_URL")
            
            if not api_key:
                raise ValueError("LLM_API_KEY is not set for OpenAI provider.")

            return OpenAI(api_key=api_key, base_url=base_url)
        else:
            raise NotImplementedError(f"LLM provider '{llm_provider}' is not supported yet.")

    def _create_agent(self):
        """
        Creates the PydanticAI agent.

        Returns:
            An instance of the PydanticAI agent.
        """
        # In the future, we will add tools and memory here
        return Agent(
            llm=self.llm,
            system_prompt=SYSTEM_PROMPT,
            # memory=... 
            # tools=...
        )

    def invoke(self, query: str) -> str:
        """
        Invokes the agent with a given query.

        Args:
            query (str): The user's query.

        Returns:
            str: The agent's response.
        """
        self.conversation_history.append({"role": "user", "content": query})
        
        # For now, we pass the history manually. Later, this will be handled by a memory system.
        response = self.agent.run(input=list(self.conversation_history))
        
        self.conversation_history.append({"role": "assistant", "content": response})
        return response

if __name__ == "__main__":
    # A simple example of how to use the agent
    agent = DynomousAgent()
    print("Dynomous: Hello! I'm Dynomous, your AI programming tutor. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        response = agent.invoke(user_input)
        print(f"Dynomous: {response}")
