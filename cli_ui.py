import os
from dotenv import load_dotenv
from memory import MemoryManager

load_dotenv()

def get_agent_response(user_id: str, user_input: str) -> str:
    """
    Placeholder function for agent interaction.
    In a real scenario, this would call the main agent logic.
    """
    # For now, just echo the input and add a simple response
    return f"Agent received: {user_input}. (This is a placeholder response)"

def main():
    user_id = "terminal_user"
    memory_manager = MemoryManager(user_id=user_id)

    print("Welcome to Dynomous AI Tutor (Terminal UI v0)!")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break

        # Get agent response (using placeholder for now)
        agent_response = get_agent_response(user_id, user_input)

        # Add user message to memory
        memory_manager.add_message(role="user", content=user_input)

        # Add agent response to memory
        memory_manager.add_message(role="assistant", content=agent_response)

        # Display conversation history (optional, can be toggled or summarized)
        print("\n--- Conversation History ---")
        history = memory_manager.get_history()
        for msg in history:
            print(f"{msg['role'].capitalize()}: {msg['content']}")
        print("--------------------------")

        print(f"Agent: {agent_response}")

if __name__ == "__main__":
    main()
