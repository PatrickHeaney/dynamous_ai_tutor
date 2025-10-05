# Increment 1: The Core Conversation Loop - Project Planning

## Project Overview
This project aims to build the simplest possible, runnable AI agent. The goal is to establish a core conversation loop where a user can interact with the agent through a terminal interface. The agent will respond using an LLM, without any tools or long-term memory. This increment serves as the foundational baseline for future development.

## Architecture

### Components
1.  **Agent Core (agent.py)**
    *   Basic agent implementation using a core AI framework.
    *   Handles communication with the LLM.
    *   Reads environment variables (LLM_BASE_URL, LLM_API_KEY, LLM_CHOICE) to dynamically configure the LLM client.
2.  **Terminal UI (cli.py)**
    *   A simple command-line interface for users to interact with the agent.
    *   Manages the conversation loop (input -> agent -> output).
3.  **System Prompt (prompt.py)**
    *   A minimal system prompt to define the agent's basic persona (e.g., "You are a helpful assistant.").

### Tech Stack
- **Pydantic AI**: Core agent framework (or similar).
- **Python 3.10+**: Base language.
- **python-dotenv**: For environment variable management (e.g., API keys).
- **pytest**: For unit testing.
- **Rich/Typer**: For an improved terminal UI experience (optional but recommended).

## System Prompt Strategy
The agent will use a static, basic system prompt that instructs the LLM to act as a general-purpose helpful assistant. The focus is on establishing the communication channel, not on complex persona or tool usage instructions.

## Agent Functionality

### Primary Features
-   Start a session from the terminal.
-   Accept multi-line user input.
-   Send the input to the LLM via the agent.
-   Stream the LLM's response back to the terminal.
-   Exit the session gracefully.
-   Configurable LLM provider (e.g., OpenAI, Ollama) via environment variables.

### Agent Input/Output Structure
-   **Input**: Natural language text from the user's terminal input.
-   **Output**: Natural language text streamed from the LLM to the user's terminal.

## Testing Strategy
-   **Unit Tests**:
    -   Verify that the agent can be initialized correctly.
    -   Test the creation of the terminal UI.
-   **Integration Tests**:
    -   A simple test to ensure the agent can receive a message and produce a non-empty response from a mocked LLM.
