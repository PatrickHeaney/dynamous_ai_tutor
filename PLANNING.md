# Dynomous AI Agent Mastery Project Planning

This document outlines the high-level design for building the MVP of our Dynomous AI Agent, which will serve as a tutor providing guidance and support throughout the AI agent development process. This agent will be built with Pydantic AI, inspired by the `4_Pydantic_AI_Agent` module from the AI Agent Mastery course, and will feature Agentic RAG capabilities, short-term and long-term memory, and the ability to search the internet.

Initially, the agent will leverage OpenAI for text and embedding generation. A subsequent version (v1) will transition to using a local Ollama LLM for enhanced control and privacy.

## System Architecture

Our system will consist of the following components:

```
                    +----------------+
                    | Streamlit UI   |
                    +--------+-------+
                             |
                    +--------v-------+
                    |   AI Agent     |
                    +--------+-------+
                             |
          +------------------+------------------+
          |                  |                  |
+---------v------+  +--------v-------+  +------v--------+
| Document Store |  | Memory System  |  |  Agent Tools  |
+---------+------+  +--------+-------+  +------+--------+
          |                  |                  |
          |         +--------v-------+          |
          +-------->| Vector Database|<---------+
                    +----------------+
```

### Key Components:

1.  **Document Processing Pipeline**
    *   **v0.1:** Local RAG pipeline for code repositories (e.g., copies of relevant codebases for examples and reference).
    *   **v0.2:** Local RAG pipeline for video tutorial transcripts.
    *   File type detection, text extraction, chunking, and embedding.

2.  **Vector Database Integration**
    *   Supabase/PostgreSQL with pgvector for document storage and retrieval.
    *   Metadata management.

3.  **Memory System**
    *   Short-term conversation memory.
    *   Long-term memory extraction and storage.
    *   Memory deduplication mechanism.

4.  **AI Agent**
    *   Pydantic AI framework for structured agent development.
    *   LLM integration:
        *   **v0:** OpenAI for text generation and embedding generation.
        *   **v1:** Local Ollama LLM for text generation and embedding generation with a more advanced model.
    *   Tool selection and execution.
    *   Agentic RAG integration.

5.  **Agent Tools**
    *   Web search (using Brave API or SearXNG).
    *   Image analysis.
    *   Code execution.
    *   SQL query generation and execution (for interacting with the document store).

6.  **Basic User Interface**
    *   Streamlit-based chat interface for interaction.
    *   Session management.

## Development Phases

The project is organized into several development phases:

### Phase 1: Core RAG Pipeline
*   **Sub-phase 1.1 (v0.1):** Build the foundation for document processing, text chunking, embedding generation, and vector database integration for local code repositories.
*   **Sub-phase 1.2 (v0.2):** Extend the RAG pipeline to process local video tutorial transcripts.

### Phase 2: Memory System
*   Implement short-term and long-term memory systems with deduplication.

### Phase 3: Agent Implementation (OpenAI)
*   Create the AI agent framework with Pydantic AI, integrating OpenAI for LLM capabilities.

### Phase 4: Agent Tools
*   Develop various tools for the agent, including web search (Brave/SearXNG), image analysis, and code execution.

### Phase 5: Basic User Interface
*   Build a simple Streamlit interface for interacting with the agent.

### Phase 6: Transition to Local Ollama (v1)
*   Migrate LLM and embedding generation to a local Ollama instance, configuring for a more advanced local model.

## Environment Configuration

The system will use environment variables for configuration, allowing flexibility in deployment scenarios. A `.env.example` file will be provided with the following structure:

```python
# Set this to either openai, openrouter, or ollama
LLM_PROVIDER=

# Base URL for the OpenAI compatible instance
LLM_BASE_URL=

# API key for OpenAI or OpenRouter (no need to set for Ollama)
LLM_API_KEY=

# The LLM you want to use for the agents.
LLM_CHOICE=

# The provider for your embedding model (openai or ollama)
EMBEDDING_PROVIDER=

# Base URL for the embedding model
EMBEDDING_BASE_URL=

# API key for your embedding model provider
EMBEDDING_API_KEY=

# The embedding model to use
EMBEDDING_MODEL_CHOICE=

# Postgres DB URL for mem0 (long-term memory)
# Format: postgresql://[user]:[password]@[host]:[port]/[database_name]
DATABASE_URL=

# Supabase configuration for RAG
SUPABASE_URL=
SUPABASE_SERVICE_KEY=

# Set your Brave API key if using Brave for agent web search (leave empty if using SearXNG)
BRAVE_API_KEY=

# Set the SearXNG endpoint if using SearXNG for agent web search (leave empty if using Brave)
SEARXNG_BASE_URL=
```

## File Structure

```
dynamous_ai_tutor/
├── .env.example               # Example environment variables
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── PLANNING.md                # This planning document
├── TASKS.md                   # Implementation tasks
├── agent.py                   # Main agent implementation
├── prompt.py                  # Prompt templates
├── tools.py                   # Agent tools
├── streamlit_ui.py            # Streamlit user interface
├── tests/                     # Test directory
│   ├── test_agent.py          # Agent tests
│   ├── test_tools.py          # Tools tests
├── RAG_Pipeline/              # RAG Pipeline components
│   ├── common/                # Common RAG functionality
│   │   ├── db_handler.py      # DB operations for RAG
│   │   ├── text_processor.py  # Functions to prep text for vector DB
│   │   └── tests/             # Tests for common components
│   ├── Code_Repositories/     # Local code repository processing
│   │   ├── main.py            # Entrypoint script to start the code repo RAG pipeline
│   │   ├── file_watcher.py    # Main logic to watch for code repo changes and insert into the vector DB
│   │   └── tests/             # Tests for code repo components
│   └── Video_Transcripts/     # Local video transcript processing
│       ├── main.py            # Entrypoint script to start the video transcript RAG pipeline
│       ├── file_watcher.py    # Main logic to watch for video transcript changes and insert into the vector DB
│       └── tests/             # Tests for video transcript components
```

## Testing Strategy

Our testing approach will cover individual components in isolation, following a Test-Driven Development (TDD) methodology. Unit tests will be written for new features, functions, and classes, ensuring expected use, edge cases, and failure scenarios are covered.

## Future Enhancements

The following enhancements are planned for future iterations:

1.  **Crawl4AI RAG Server Integration:** Explore integrating a Crawl4AI RAG Server for processing and storing helpful website content.
2.  **Advanced React-based Frontend:** Develop a more interactive and visually rich UI.
3.  **Containerization with Docker:** Implement Docker for reproducible development and deployment environments.
4.  **Additional Data Sources:** Expand RAG capabilities to include other data sources beyond code repositories and video transcripts.
