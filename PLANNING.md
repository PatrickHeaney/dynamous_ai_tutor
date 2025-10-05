# Increment 1: The Core Conversation Loop - Project Planning

## Project Overview
This project aims to build the simplest possible, runnable AI agent, establishing a foundational baseline for future development. The goal is to create a core conversation loop where a user can interact with the agent through a terminal interface. The agent will respond using an LLM, without any tools or long-term memory.

The implementation will draw inspiration from the Pydantic AI weather agent example (https://ai.pydantic.dev/examples/weather-agent/) and the basic agent example found at `/Users/pmh/code/_new_prj/example_code/ai-agent-mastery/4_Pydantic_AI_Agent/extras/Basic_Pydantic_AI_Agent`.

## Architecture

### Components
  1.  **Agent Core (`agent.py`)**: The main agent logic, responsible for communicating with the LLM. It will be configured dynamically using environment variables.
  2.  **Terminal UI (`cli.py`)**: A command-line interface for user interaction, managing the input-output loop.
  3.  **System Prompt (`prompts.py`)**: A module to store the initial system prompt defining the agent's persona.

### File Structure
The project will follow a standard Python application layout to promote modularity and clarity.
```
/
├── .env
├── .gitignore
├── PLANNING.md
├── README.md
├── pyproject.toml
└── src/
    ├── __init__.py
    ├── agent.py
    ├── cli.py
    └── prompts.py
└── tests/
    ├── __init__.py
    └── test_agent.py
```

### Tech Stack
  - **Python 3.10+**: Base language.
  - **uv**: For package and environment management.
  - **Pydantic AI**: Core agent framework.
  - **python-dotenv**: For loading environment variables from a `.env` file.
  - **Rich/Typer**: For a polished command-line interface.
  - **pytest**: For unit and integration testing.

### Assumptions
- The development environment will use **uv** for package and virtual environment management.
- The user has Python 3.10+ installed.
- LLM credentials and configuration (API Key, Base URL, Model Name) will be managed via a `.env` file, as specified in `.env.example`.
- The initial implementation will be stateless, with no memory between conversation turns or sessions.
- The project will follow the structure and conventions outlined in the `GEMINI.md` guide.

## System Prompt Strategy
The agent will use a static, basic system prompt that instructs the LLM to act as a general-purpose helpful assistant. The focus is on establishing the communication channel, not on complex persona or tool usage instructions.

## Agent Functionality

### Primary Features
  - Start a session from the terminal.
  - Accept multi-line user input.
  - Send the input to the LLM via the agent.
  - Stream the LLM's response back to the terminal.
  - Exit the session gracefully.
  - Configurable LLM provider (e.g., OpenAI, Ollama) via environment variables.

### Agent Input/Output Structure
  - **Input**: Natural language text from the user's terminal input.
  - **Output**: Natural language text streamed from the LLM to the user's terminal.

## Testing Strategy
-   **Unit Tests**:
    -   Verify that the Agent Core can be initialized correctly, including the dynamic loading of LLM configuration.
    -   Test the Terminal UI creation and input/output handling logic in isolation.
-   **Integration Tests**:
    -   Create a test that simulates a user interaction, ensuring the Terminal UI and Agent Core work together as expected.
    -   This test will use a mocked LLM to provide a predictable response, confirming the end-to-end conversation loop without making a real API call.
