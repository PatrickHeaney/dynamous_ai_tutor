"""
This module defines the core AI agent for the Dynomous AI Tutor.
"""
import os
from pydantic_ai import Agent
from openai import OpenAI
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT
from memory import MemoryManager

# Load environment variables from .env file
load_dotenv()

class DynomousAgent:
    """
    The main class for the Dynomous AI Tutor agent.
    """
    def __init__(self, user_id: str = "default_user"):
        """
        Initializes the DynomousAgent.
        """
        self.llm = self._initialize_llm()
        self.memory = MemoryManager(user_id=user_id)
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
        # In the future, we will add tools here
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
        self.memory.add_message(role="user", content=query)
        
        # Retrieve conversation history and relevant memories
        history = self.memory.get_history()
        relevant_memories = self.memory.search(query)
        
        # Combine history and memories for context
        context = "\n".join([m['content'] for m in relevant_memories])
        
        # For now, we prepend the context to the query.
        # A more sophisticated approach would be to format this into the prompt.
        enriched_query = f"Relevant context:\n{context}\n\nUser query: {query}"

        response = self.agent.run(input=history + [{ "role": "user", "content": enriched_query }])
        
        self.memory.add_message(role="assistant", content=response)
        return response

if __name__ == "__main__":
    # A simple example of how to use the agent
    agent = DynomousAgent(user_id="cli_user")
    print("Dynomous: Hello! I'm Dynomous, your AI programming tutor. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        response = agent.invoke(user_input)
        print(f"Dynomous: {response}")
