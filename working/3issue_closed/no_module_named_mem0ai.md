Updates
9/23/2025 - fixed 🎉
  ```Use
  from mem0 import Memory instead of mem0ai.

  Here are the docs which you can refer to:
  
  https://docs.mem0.ai/platform/quickstart
  
  https://docs.mem0.ai/open-source/python-quickstart```

9/22/2025
 - posted issue to https://github.com/mem0ai/mem0/issues/3493
 - posted iso help to https://community.dynamous.ai/c/ai-mastery-course/
 - created new open source repository for where I encountered the ModuleNotFoundError, https://github.com/PatrickHeaney/dynamous_ai_tutor

I'm working on a project using Python 3.13.7 on macOS, managing my virtual environment and packages with uv. I'm encountering a very stubborn
  ModuleNotFoundError: No module named 'mem0ai' when trying to import the mem0ai library, both within my project's modules (e.g., memory.py) and directly from
  the Python interpreter within the activated virtual environment. This issue prevents me from running any unit tests that depend on mem0ai.

Project Setup:
  * OS: macOS
  * Python Version: 3.13.7
  * Virtual Environment/Package Manager: uv (version 0.8.5)
  * mem0ai is listed in requirements.txt.
  * Project structure includes a tests/ directory with an __init__.py file.

Troubleshooting Steps Taken (and their outcomes):

  1. Initial `uv pip install -r requirements.txt`: Reported success, but ModuleNotFoundError persisted.
  2. Explicit `uv pip install mem0ai`: Reported success, but ModuleNotFoundError persisted.
  3. Direct `python -c "import mem0ai"` within activated `.venv`: Failed with ModuleNotFoundError. This indicates the issue is not specific to pytest but to the
    module's importability itself.
  4. Removed and recreated `.venv`: rm -rf .venv followed by uv venv .venv and uv pip install -r requirements.txt. Reported success, but ModuleNotFoundError
    persisted.
  5. Cleared `uv` cache: uv clean. Reinstalled mem0ai. ModuleNotFoundError persisted.
  6. Ensured `pip` is available and tried `python -m pip install mem0ai`: Reported Requirement already satisfied, confirming mem0ai is supposedly installed.
    ModuleNotFoundError persisted.
  7. Set `PYTHONPATH` explicitly: export PYTHONPATH=/path/to/project/root before running pytest. ModuleNotFoundError persisted.
  8. Added `__init__.py` to `tests/` directory: No change.
  9. Added `sys.path.insert(0, str(Path(__file__).parent.parent))` to test files: No change, as the error originates from memory.py trying to import mem0ai, not
    from the test file trying to import memory.

Exact Error Traceback (from `python -m pytest tests/test_memory.py`):

  1 ============================= test session starts ==============================
  2 platform darwin -- Python 3.13.7, pytest-8.4.2, pluggy-1.6.0
  3 rootdir: /Users/pmh/code/ai-agent-mastery/dynamous_ai_tutor
  4 plugins: anyio-4.10.0, logfire-4.8.0
  5 collected 0 items / 1 error
  6
  7 ==================================== ERRORS ====================================
  8 ____________________ ERROR collecting tests/test_memory.py _____________________
  9 ImportError while importing test module '/Users/pmh/code/ai-agent-mastery/dynamous_ai_tutor/tests/test_memory.py'.
  10 Hint: make sure your test modules/packages have valid Python names.
  11 Traceback:
  12 /opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
  13     return _bootstrap._gcd_import(name[level:], package, level)
  14            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  15 tests/test_memory.py:13: in <module>
  16     from memory import MemoryManager
  17 memory.py:5: in <module>
  18     from mem0ai import Mem0
  19 E   ModuleNotFoundError: No module named 'mem0ai'
  20 =========================== short test summary info ============================
  21 ERROR tests/test_memory.py
  22 !!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
  23 =============================== 1 error in 0.05s ===============================

I'm at a loss as to why mem0ai cannot be imported despite all indications that it's installed. It seems like a very specific environment or compatibility
issue.

Has anyone encountered a similar problem with mem0ai, uv, or Python 3.13.7? Any insights or suggestions would be greatly appreciated!
