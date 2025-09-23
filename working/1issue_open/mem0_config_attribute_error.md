---
name: AttributeError: 'dict' object has no attribute 'custom_fact_extraction_prompt' during Memory initialization
about: The mem0.Memory class raises an AttributeError when initializing with a config dictionary, specifically when accessing 'custom_fact_extraction_prompt'.
title: AttributeError: 'dict' object has no attribute 'custom_fact_extraction_prompt'
labels: bug, configuration
assignees: ''

---

**Describe the bug**
When attempting to initialize the `mem0.Memory` class by passing a `config` dictionary, an `AttributeError: 'dict' object has no attribute 'custom_fact_extraction_prompt'` is raised. This occurs even when `custom_fact_extraction_prompt` is explicitly included (or set to `None`) within the top-level `config` dictionary, as per the documentation's implied structure.

This issue prevents the successful instantiation of `mem0.Memory`, blocking further development.

**Attempts to use `Config` class:**
I also attempted to import and use a `Config` class, first from `mem0` directly (`from mem0 import Memory, Config`) and then from `mem0.configs` (`from mem0.configs import Config` and `from mem0.configs import configs`), based on hints from `ImportError` messages. Both attempts resulted in `ImportError`s, indicating that a `Config` class is either not directly exposed or not named as expected.

**To Reproduce**
Steps to reproduce the behavior:

1.  **Environment Setup:**
    *   OS: macOS
    *   Python Version: 3.13.7
    *   Package Manager: `uv` (version 0.8.5)
    *   `mem0ai` Version: Installed via `uv pip install mem0ai` (latest available as of 2025-09-23)
2.  **Minimal Code:**
    Create a Python file (e.g., `test_mem0_config.py`) with the following content:
    ```python
    import os
    from mem0 import Memory
    from dotenv import load_dotenv

    load_dotenv() # Ensure .env is loaded if using environment variables

    # Ensure these environment variables are set in your .env file
    # SUPABASE_URL=your_supabase_url
    # SUPABASE_KEY=your_supabase_key
    # LLM_PROVIDER=openai
    # OPENAI_API_KEY=your_openai_api_key
    # EMBEDDING_PROVIDER=openai
    # OPENAI_EMBEDDING_API_KEY=your_openai_embedding_api_key

    try:
        memory_instance = Memory(
            config={
                "vector_store": {
                    "provider": "supabase",
                    "config": {
                        "url": os.getenv("SUPABASE_URL"),
                        "key": os.getenv("SUPABASE_KEY"),
                    }
                },
                "llm": {
                    "provider": os.getenv("LLM_PROVIDER"),
                    "config": {
                        "api_key": os.getenv("OPENAI_API_KEY"),
                    }
                },
                "embedder": {
                    "provider": os.getenv("EMBEDDING_PROVIDER"),
                    "config": {
                        "api_key": os.getenv("OPENAI_EMBEDDING_API_KEY"),
                    }
                },
                "custom_fact_extraction_prompt": None, # Explicitly set
            }
        )
        print("Memory initialized successfully!")
    except AttributeError as e:
        print(f"Caught AttributeError: {e}")
    except Exception as e:
        print(f"Caught unexpected exception: {e}")
    ```
3.  **Run the script:**
    `python test_mem0_config.py`

**Expected behavior**
The `mem0.Memory` class should initialize successfully without raising an `AttributeError`.

**Actual behavior**
An `AttributeError` is raised during initialization:

```
Traceback (most recent call last):
  File "/Users/pmh/code/ai-agent-mastery/dynamous_ai_tutor/cli_ui.py", line 46, in <module>
    main()
    ~~~~^^
  File "/Users/pmh/code/ai-agent-mastery/dynamous_ai_tutor/cli_ui.py", line 17, in main
    memory_manager = MemoryManager(user_id=user_id)
  File "/Users/pmh/code/ai-agent-mastery/dynamous_ai_tutor/memory.py", line 25, in __init__
    self.memory = Memory(
                  ~~~~~~^
        config={
        ^^^^^^^^
    ...<20 lines>...
        }
        ^
    )
    ^
  File "/Users/pmh/code/ai-agent-mastery/dynamous_ai_tutor/.venv/lib/python3.13/site-packages/mem0/memory/main.py", line 126, in __init__
    self.custom_fact_extraction_prompt = self.config.custom_fact_extraction_prompt
                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'dict' object has no attribute 'custom_fact_extraction_prompt'
```

**Analysis/Possible Cause**
The traceback indicates that within `mem0/memory/main.py`, the `self.config` object is a standard Python dictionary, but the code attempts to access `custom_fact_extraction_prompt` as an *attribute* of this dictionary (e.g., `self.config.custom_fact_extraction_prompt`). Dictionaries do not have attributes; their elements are accessed via keys (e.g., `self.config['custom_fact_extraction_prompt']` or `self.config.get('custom_fact_extraction_prompt')`).

This suggests that the `mem0` library's internal `Memory` class `__init__` method is either:
1.  Incorrectly assuming that the `config` object passed to it is an object with attributes (e.g., a Pydantic model instance) rather than a raw dictionary.
2.  Failing to properly convert the input `config` dictionary into its internal configuration object before attempting to access its properties.

**Suggested Fix (for `mem0` maintainers)**
In `mem0/memory/main.py`, line 126 (and potentially other similar lines accessing `self.config` properties), consider changing attribute access to dictionary key access, for example:
`self.custom_fact_extraction_prompt = self.config.get('custom_fact_extraction_prompt')`
or ensure that `self.config` is always an object with attributes before this line is executed.