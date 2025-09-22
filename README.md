# Dynomous AI Agent: Your AI Agent Development Tutor

A powerful AI agent built with Pydantic AI, designed to serve as a tutor, providing guidance and support throughout the AI agent development process. This agent combines Agentic RAG (Retrieval Augmented Generation), long-term memory, web search, image analysis, and code execution capabilities. It is inspired by the `4_Pydantic_AI_Agent` module from the AI Agent Mastery course.

Initially, the agent will leverage OpenAI for text and embedding generation. A subsequent version (v1) will transition to using a local Ollama LLM for enhanced control and privacy.

## Agent Capabilities

-   **Agentic RAG**: Query your documents with context-aware intelligence from:
    *   Local code repositories (v0.1)
    *   Local video tutorial transcripts (v0.2)
-   **Long-term Memory**: The agent remembers important information from previous conversations.
-   **Web Search**: Search the internet using Brave API or SearXNG.
-   **Image Analysis**: Analyze images with vision-capable LLMs.
-   **Code Execution**: Generate and run Python code safely.
-   **Multi-LLM Support**: Works with OpenAI (v0) and local Ollama models (v1).
-   **User Interfaces**: Interact via a simple terminal UI (v0) or a Streamlit UI (v1).

## Project Structure

```
dynamous_ai_tutor/
├── .env.example               # Example environment variables
├── requirements.txt           # Project dependencies
├── README.md                  # This project documentation
├── PLANNING.md                # High-level design and planning document
├── TASKS.md                   # Detailed implementation tasks
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
│   │   ├── file_watcher.py    # Logic to watch for code repo changes
│   │   └── tests/             # Tests for code repo components
│   └── Video_Transcripts/     # Local video transcript processing
│       ├── main.py            # Entrypoint script to start the video transcript RAG pipeline
│       ├── file_watcher.py    # Logic to watch for video transcript changes
│       └── tests/             # Tests for video transcript components
```

## Setup Instructions

### Prerequisites

-   Python 3.11+
-   Supabase project (cloud or self-hosted)
-   API keys for OpenAI (for v0 LLM/embeddings)
-   Brave API key (optional, for web search)
-   SearXNG endpoint (optional, for local web search)
-   Deno (optional, for code execution)

#### For Local Ollama/SearXNG (v1 and local setup):

-   [Local AI package installed](https://github.com/coleam00/local-ai-packaged) (recommended for self-hosting Ollama and SearXNG)

### Environment Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd dynamous_ai_tutor
    ```

2.  **Create and activate virtual environment and install dependencies:**
    ```bash
    uv venv
    source .venv/bin/activate # On macOS/Linux
    # .venv\Scripts\activate # On Windows
    uv pip install -r requirements.txt
    ```

3.  **Create and configure `.env` file:**
    Copy the example environment file and fill in your credentials:
    ```bash
    cp .env.example .env
    ```
    Edit the `.env` file with your specific configurations:

    ```env
    # Set this to either openai, openrouter, or ollama
    LLM_PROVIDER=openai

    # Base URL for the OpenAI compatible instance
    LLM_BASE_URL=https://api.openai.com/v1

    # API key for OpenAI or OpenRouter (no need to set for Ollama)
    LLM_API_KEY=your_openai_api_key_here

    # The LLM you want to use for the agents.
    LLM_CHOICE=gpt-4o-mini # Example: gpt-4o-mini, qwen2.5:14b-instruct-8k (for Ollama)

    # The provider for your embedding model (openai or ollama)
    EMBEDDING_PROVIDER=openai

    # Base URL for the embedding model
    EMBEDDING_BASE_URL=https://api.openai.com/v1

    # API key for your embedding model provider
    EMBEDDING_API_KEY=your_openai_api_key_here

    # The embedding model to use
    EMBEDDING_MODEL_CHOICE=text-embedding-3-small # Example: text-embedding-3-small, nomic-embed-text (for Ollama)

    # Postgres DB URL for mem0 (long-term memory)
    # Format: postgresql://[user]:[password]@[host]:[port]/[database_name]
    DATABASE_URL=postgresql://postgres:password@localhost:5432/mydb

    # Supabase configuration for RAG
    SUPABASE_URL=your_supabase_url
    SUPABASE_SERVICE_KEY=your_supabase_service_key

    # Set your Brave API key if using Brave for agent web search (leave empty if using SearXNG)
    BRAVE_API_KEY=

    # Set the SearXNG endpoint if using SearXNG for agent web search (leave empty if using Brave)
    SEARXNG_BASE_URL=
    ```

### Database Setup

1.  **Create a Supabase project** at [https://supabase.com](https://supabase.com) (or use a self-hosted instance).
2.  **Navigate to the SQL Editor** in your Supabase dashboard.
3.  **Run the necessary SQL scripts** to create tables for RAG (documents, document_metadata, document_rows) and long-term memory (e.g., user_profiles, conversations, messages). Also, create the RPC function for secure SQL queries.
    *   *Note:* I will switch to a local embedding model later.  I'm starting with openai first. When using a local Ollama embedding model with different dimensions (e.g., 768 instead of 1536), remember to adjust the vector dimensions in the SQL scripts before running them.

### Running the RAG Pipelines

Activate the `venv_rag` virtual environment and run the desired pipeline:

#### Code Repositories Pipeline (v0.1)

1.  Configure `RAG_Pipeline/Code_Repositories/config.json` to specify the local directories to watch.
2.  Run the pipeline:
    ```bash
    cd RAG_Pipeline
    source venv_rag/bin/activate
    python Code_Repositories/main.py
    ```

#### Video Transcripts Pipeline (v0.2)

1.  Configure `RAG_Pipeline/Video_Transcripts/config.json` to specify the local directories to watch.
2.  Run the pipeline:
    ```bash
    cd RAG_Pipeline
    source venv_rag/bin/activate
    python Video_Transcripts/main.py
    ```

### Running the Agent

#### v0: Terminal UI
1.  Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
2.  Run the terminal UI:
    ```bash
    python cli_ui.py
    ```

#### v1: Streamlit UI
1.  Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
2.  Run the Streamlit UI:
    ```bash
    streamlit run streamlit_ui.py
    ```
3.  Open your browser to the URL shown in the terminal (typically `http://localhost:8501`).

### Code Execution MCP Server Setup (Optional)

To enable code execution, you need to install Deno and run the MCP server in a separate terminal:

1.  Install Deno from [https://deno.land/](https://deno.land/).
2.  Run the server:
    ```bash
    deno run -N -R=node_modules -W=node_modules --node-modules-dir=auto jsr:@pydantic/mcp-run-python sse
    ```
3.  Uncomment the `mcp_servers=[code_execution_server]` line in `agent.py` to enable code execution.

## Troubleshooting

-   **Vector Dimensions Mismatch**: Ensure the embedding dimensions in your database match the model you're using. OpenAI models typically use 1536 dimensions, while some Ollama models (e.g., `nomic-embed-text`) use 768. Adjust Supabase SQL scripts if necessary.
-   **Function Calling Support**: Not all LLMs support function calling. If using Ollama, ensure your chosen model supports this feature.
-   **Database Connection**: Verify your Supabase URL and service key in the `.env` file. Check Supabase logs for connection errors.

## Future Enhancements

-   **Crawl4AI RAG Server Integration:** Integrate a Crawl4AI RAG Server for processing and storing helpful website content.
-   **Advanced React-based Frontend:** Develop a more interactive and visually rich UI.
-   **Containerization with Docker:** Implement Docker for reproducible development and deployment environments.
-   **Multi-Agent Architecture:** Explore multi-agent architectures using LangGraph and guardrails to enhance tutor capabilities and reliability.
-   **Additional Data Sources:** Expand RAG capabilities to include other data sources.
