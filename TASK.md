# Increment 1: The Core Conversation Loop - Task List

## 1. Environment & Project Setup
- [ ] Create and activate a virtual environment: `uv venv`
- [ ] Initialize the `src` and `tests` directories.
- [ ] Create empty files: `src/__init__.py`, `src/agent.py`, `src/cli.py`, `src/prompts.py`, `tests/__init__.py`, `tests/test_agent.py`.
- [ ] Create `pyproject.toml` and add initial dependencies using `uv add`:
    - `uv add pydantic-ai`
    - `uv add python-dotenv`
    - `uv add rich`
    - `uv add typer`
    - `uv add --dev pytest`
- [ ] Verify `.env.example` exists with placeholders for `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_CHOICE`.
- [ ] Create a local `.env` file for development.
- [ ] Ensure `.gitignore` is present and configured for Python projects (e.g., ignores `.venv`, `__pycache__`, `.env`).

## 2. Core Agent Implementation
- [ ] In `src/prompts.py`, create a minimal system prompt (e.g., "You are a helpful assistant.").
- [ ] In `src/agent.py`:
    - [ ] Load `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_CHOICE` from the `.env` file.
    - [ ] Add logic to handle default values if variables are not set.
    - [ ] Dynamically initialize the Pydantic AI client using the loaded environment variables.
    - [ ] Define a core function to handle a single conversation turn, taking user input and returning the LLM's response.

## 3. Terminal UI
- [ ] In `src/cli.py`, set up a Typer application.
- [ ] Implement a main loop to:
    - [ ] Prompt the user for input using Rich.
    - [ ] Send the input to the agent core function.
    - [ ] Stream the agent's response to the console.
    - [ ] Handle graceful exit (e.g., with `Ctrl+C` or an "exit" command).

## 4. Testing
- [ ] In `tests/test_agent.py`:
    - [ ] Write a unit test to verify the agent initializes correctly with and without environment variables.
    - [ ] Write an integration test using a mocked LLM to confirm the end-to-end loop (CLI -> Agent -> Mocked LLM -> CLI) works as expected.
- [ ] Run tests using `uv run pytest` and ensure they pass.

## 5. Documentation
- [ ] Update `README.md` to describe the project's purpose, how to set it up (using `uv`), and how to run it for Increment 1.

## Milestone: Increment 1 Completion
- [ ] All tasks above are completed.
- [ ] The agent is runnable from the terminal via the `cli.py` entry point.
- [ ] A user can have a basic, stateless conversation with a configurable LLM backend.
- [ ] All tests pass.
