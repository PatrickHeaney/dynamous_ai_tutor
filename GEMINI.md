### 🔄 Project Awareness & Context
- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check `TASK.md`** before starting a new task. If the task isn’t listed, add it with a brief description and today's date.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.

### 🧠 AI Behavior Rules
- **Never assume missing context. Ask questions if uncertain.**
- **Always confirm file paths & module names** exist before using
- **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.

### 🧱 Code Structure & Modularity
- **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.
  For agents this looks like:
    - `agent.py` - Main agent definition and execution logic
    - `tools.py` - Tool functions used by the agent
    - `prompts.py` - System prompts
- **Use clear, consistent imports** (prefer relative imports within packages).

### 🧪 Testing & Reliability
- **Always create Pytest unit tests for new features** (functions, classes, routes, etc).
- **After updating any logic**, check whether existing unit tests need to be updated. If so, do it.
- **Tests should live in a `/tests` folder** mirroring the main app structure.
  - Include at least:
    - 1 test for expected use
    - 1 edge case
    - 1 failure case
- Always test the individual functions for agent tools.

### ✅ Task Completion
- **Mark completed tasks in `TASK.md`** immediately after finishing them.
- Add new sub-tasks or TODOs discovered during development to `TASK.md` under a “Discovered During Work” section.

### 📎 Style & Conventions
- **Use Python** as the primary language. Use uv to install, manage dependencies, and run the application.
- **Follow PEP8**, use type hints, and format with `black`.
- **Use `rich` for rich text output**.
- **Use `pydantic` for data validation**.
- Write **docstrings for every function** using the Google style:
  ```python
  def example():
      """
      Brief summary.

      Args:
          param1 (type): Description.

      Returns:
          type: Description.
      """
  ```

### 📚 Documentation & Explainability
- **Update `README.md`** when new features are added, dependencies change, or setup steps are modified.
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
- When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.

## 🧠 Lessons Learned

### Debugging Silent Streaming API Failures
- **Symptom**: An application using a streaming API (e.g., from an LLM client library) fails to produce output and does not raise any exceptions. It may appear to hang or simply loop.
- **Cause**: This often indicates a silent failure where the API returns an empty or immediately closed stream due to an underlying issue like an invalid API key, incorrect endpoint URL, billing problems, or an invalid model name.
- **Solution**: A standard `try...except` block may not catch the error. The most effective debugging strategy is to **temporarily disable streaming** (e.g., set `stream=False` in the API call). A non-streaming, blocking request is much more likely to raise a specific, descriptive exception (e.g., `AuthenticationError`, `NotFoundError`) that will reveal the root cause of the problem.
