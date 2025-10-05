# Increment 1: The Core Conversation Loop - Task List

## 1. Project Setup & Configuration
- [ ] Initialize project structure (`agent.py`, `cli.py`, `prompt.py`).
- [ ] Set up `requirements.txt` with initial dependencies (pydantic-ai, python-dotenv, rich, etc.).
- [ ] Create `.env.example` with placeholders for `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_CHOICE`.
- [ ] Ensure `.gitignore` is present and configured for Python projects.
- [ ] Update `README.md` to describe the goal and setup for Increment 1.

## 2. Core Agent Implementation
- [ ] Create `prompt.py` with a minimal system prompt (e.g., "You are a helpful assistant.").
- [ ] Create `agent.py` to:
    - [ ] Load `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_CHOICE` from the environment.
    - [ ] Add logic to handle default values if variables are not set.
    - [ ] Dynamically initialize the Pydantic AI client using the loaded environment variables.
    - [ ] Define a simple function to handle a conversation turn.

## 3. Terminal UI
- [ ] Create `cli.py` to serve as the entry point.
- [ ] Implement a main loop to:
    - [ ] Prompt the user for input.
    - [ ] Send the input to the agent.
    - [ ] Stream the agent's response to the console.
    - [ ] Handle graceful exit (e.g., with `Ctrl+C` or an "exit" command).

## 4. Testing
- [ ] Set up the `tests/` directory and `pytest` configuration.
- [ ] Write a unit test to verify the agent initializes correctly with different environment variable settings.
- [ ] Write a unit test to verify the CLI starts (can be a simple mock test).
- [ ] Run the unit test and correct any issues.
- [ ] Write a simple integration test to ensure a message sent to the agent returns a (mocked) response.

## Discovered During Work
- [ ] (Add any new tasks that come up here)

## Milestone: Increment 1 Completion
- [ ] All tasks above are completed.
- [ ] The agent is runnable from the terminal.
- [ ] A user can have a basic, stateless conversation with a configurable LLM backend.
