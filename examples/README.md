# Dynamous AI Agent Mastery Pydantic Agent

A powerful AI agent built with Pydantic AI for the Dynamous AI Agent Mastery course that combines Agentic RAG (Retrieval Augmented Generation), long-term memory, web search, image analysis, and code execution capabilities. This agent can be configured to run with either cloud-based or local LLMs. The RAG pipeline implementation has also been created in a way where you can build in your own data source as another pipeline very easily.

### The goal of this agent is twofold:

1. To show you how to build an AI agent in Python to graduate from no-code tools and create the foundation for a truly production-ready AI agent.

2. To demonstrate a powerful AI agent (a Python version of the n8n prototype) with a large set of tools. No matter the AI agent you want to build for your own use case, there will certainly be components of this agent (RAG, long term memory, etc.) that you can take for yourself and incorporate into your code, even if it isn't built with the same agent framework!

## Agent Capabilities

- **Agentic RAG**: Query your documents with context-aware intelligence (local or Google Drive files)
- **Long-term Memory**: The agent remembers important information from previous conversations
- **Web Search**: Search the internet using Brave API or SearXNG
- **Image Analysis**: Analyze images with vision-capable LLMs
- **Code Execution**: Generate and run Python code safely
- **Multi-LLM Support**: Works with OpenAI, OpenRouter, or local Ollama models
- **Streamlit UI**: Simple chat interface for interacting with the agent (full frontend in a later module)

## Project Structure

```
4_Pydantic_AI_Agent/
├── .env.example               # Example environment variables
├── requirements.txt           # Project dependencies
├── agent.py                   # Main Pydantic AI agent implementation
├── clients.py                 # Client config for LLMs, databases, and long term memory
├── prompt.py                  # System prompt template
├── tools.py                   # Agent tool implementations
├── streamlit_ui.py            # Basic Streamlit user interface
├── RAG_Pipeline/              # RAG Pipeline components
│   ├── common/                # Common RAG functionality
│   │   ├── db_handler.py      # DB operations for RAG
│   │   ├── text_processor.py  # Functions to prep text for vector DB
│   ├── Google_Drive/          # Google Drive integration
│   │   ├── main.py            # Entrypoint for Google Drive RAG pipeline
│   │   ├── drive_watcher.py   # Logic for Google Drive file processing
│   ├── Local_Files/           # Local file processing
│   │   ├── main.py            # Entrypoint for local file RAG pipeline
│   │   ├── file_watcher.py    # Logic for local file processing
```

## Setup Instructions

### Prerequisites

- Python 3.11+

#### If running the agent locally:

- [Local AI package installed](https://github.com/coleam00/local-ai-packaged) (recommended)

OR

Locally hosted:
- Supabase
- Ollama
- SearXNG

#### If not running the agent locally:

- Supabase project
- API keys for LLM provider (OpenAI or OpenRouter)
- Brave API key
- [Optional] Google Drive API credentials (if using Google Drive RAG pipeline)

### Environment Setup

1. Clone the repository (if not already done)

2. Create and activate a virtual environment for the agent:

```bash
# Navigate to the project directory
cd AI_Agents_Mastery/4_Pydantic_AI_Agent

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

3. Create a separate virtual environment for the RAG pipeline:

```bash
# Navigate to the RAG Pipeline directory
cd RAG_Pipeline

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

4. Create a `.env` file by copying the `.env.example` file:

```bash
# From the main project directory
copy .env.example .env
# On macOS/Linux:
# cp .env.example .env
```

5. Configure your `.env` file with the appropriate values:

### Environment Configuration

#### LLM Configuration

```
# The provider for your LLM (openai, openrouter, or ollama)
LLM_PROVIDER=openai

# Base URL for the OpenAI compatible instance
# OpenAI: https://api.openai.com/v1
# Ollama: http://localhost:11434/v1
# OpenRouter: https://openrouter.ai/api/v1
LLM_BASE_URL=https://api.openai.com/v1

# API key for your LLM provider
LLM_API_KEY=your_api_key_here

# The LLM model to use (must support tools/function calling)
# OpenAI example: gpt-4o-mini
# OpenRouter example: anthropic/claude-3.7-sonnet
# Ollama example: qwen2.5:14b-instruct-8k
LLM_CHOICE=gpt-4o-mini

# Vision LLM for image analysis
VISION_LLM_CHOICE=gpt-4o-mini
```

#### Embedding Configuration

```
# The provider for your embedding model (openai or ollama)
EMBEDDING_PROVIDER=openai

# Base URL for the embedding model
EMBEDDING_BASE_URL=https://api.openai.com/v1

# API key for your embedding model provider
EMBEDDING_API_KEY=your_api_key_here

# The embedding model to use
# OpenAI example: text-embedding-3-small
# Ollama example: nomic-embed-text
EMBEDDING_MODEL_CHOICE=text-embedding-3-small
```

#### Database Configuration

```
# Postgres DB URL for mem0 (long-term memory)
# Format: postgresql://[user]:[password]@[host]:[port]/[database_name]
DATABASE_URL=postgresql://postgres:password@localhost:5432/mydb

# Supabase configuration for RAG
SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_KEY=your_supabase_service_key
```

#### Web Search Configuration

```
# Brave API key (leave empty if using SearXNG)
BRAVE_API_KEY=your_brave_api_key

# SearXNG endpoint (leave empty if using Brave)
# Local AI setup: http://localhost:8080 or http://searxng:8080 if in Docker
SEARXNG_BASE_URL=
```

## Database Setup

### Cloud Implementation

1. Create a Supabase project at [https://supabase.com](https://supabase.com) if you haven't already done so for the n8n prototype.

2. Create the necessary tables by running the SQL scripts in the `sql` directory:
   - Navigate to the SQL Editor in Supabase
   - Run each of the following SQL scripts:
     - `sql/documents.sql`: Creates the documents table with vector embeddings
     - `sql/document_metadata.sql`: Creates the document metadata table
     - `sql/document_rows.sql`: Creates the table for tabular data
     - `sql/execute_sql_rpc.sql`: Creates the RPC function for executing SQL queries

   **Note:** You must execute the `execute_sql_rpc.sql` script even if you followed along with the prototype. This creates a secure RPC function that allows the agent to execute read-only SQL queries against your document data.

   > **Note:** If you already created these tables for the n8n prototype, you can skip this step. The tables are exactly the same!

### Local Implementation

If you're using the Local AI package or a self-hosted Supabase instance:

1. Navigate to the SQL Editor tab in Supabase (http://localhost:8000 for your Supabase dashboard by default)

2. Run the same SQL scripts mentioned above:
   - `sql/documents.sql`
   - `sql/document_metadata.sql`
   - `sql/document_rows.sql`

   > **Important:** For local Ollama implementations using models like nomic-embed-text, you'll need to modify the vector dimensions in the SQL scripts from 1536 to 768 (or whatever the dimensions are for your embedding model) before running them.

   > **Note:** You may have already created these tables for the n8n prototype, but since this project is unified with the cloud implementation unlike in n8n, you will have to delete and recreate the documents (previously 'documents_pg') and document_metadata tables!

## Running the RAG Pipeline

The RAG Pipeline processes documents and stores them in the vector database for retrieval by the agent. You can run either the Google Drive pipeline or the Local Files pipeline. The structure of `RAG_Pipeline` is also set up in a way where you can very easily create your own pipeline for another service like Dropbox, SharePoint, Confluence, etc. Just use one of the existing pipelines as an example and all the common tooling in the `RAG_Pipeline/common/` folder.

### Local Files Pipeline

1. Configure the Local Files pipeline:
   - Edit `RAG_Pipeline/Local_Files/config.json` to specify the directories to watch
   - Example:
     ```json
     {
       ... rest of config,
       "watch_directory": "your/folder/to/watch"
     }
     ```

2. Activate the RAG Pipeline virtual environment:
   ```bash
   # Navigate to the RAG Pipeline directory
   cd RAG_Pipeline
   
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   # source venv/bin/activate
   ```

3. Run the Local Files pipeline:
   ```bash
   python Local_Files/main.py
   ```

This script will now run continuously and check each minute (this value is configurable with the --internval [seconds] parameter) for any new, updated, or deleted files and sync that with the Supabase knowledge base. This will recursively search through any subfolders of the path you provide as well!

### Google Drive Pipeline

1. Set up Google Drive API credentials:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Google Drive API (search for Google Drive at the top and click "Enable")
   - Create OAuth 2.0 credentials (choose "Desktop App" when prompted for the application type)
   - Download the credentials JSON file and save it as `RAG_Pipeline/Google_Drive/credentials.json`

2. Configure the Google Drive pipeline:
   - Edit `RAG_Pipeline/Google_Drive/config.json` to specify the folders to watch
   - Example:
     ```json
     {
       ... rest of config,
       "watch_directory": "your_google_drive_folder_id"
     }  
     ```

3. Activate the RAG Pipeline virtual environment:
   ```bash
   # Navigate to the RAG Pipeline directory
   cd RAG_Pipeline
   
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   # source venv/bin/activate
   ```

4. Run the Google Drive pipeline:
   ```bash
   python Google_Drive/main.py
   ```
   - On first run, you'll be prompted to authenticate with Google

This script will now run continuously and check each minute (this value is configurable with the --internval [seconds] parameter) for any new, updated, or deleted files and sync that with the Supabase knowledge base. This will recursively search through any subfolders of the parent folder ID you you provide as well!   

## Running the Agent

### Running the Streamlit UI

1. Activate the agent's virtual environment:
   ```bash
   # Navigate to the project directory
   cd AI_Agents_Mastery/4_Pydantic_AI_Agent
   
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   # source venv/bin/activate
   ```

2. Run the Streamlit UI:
   ```bash
   streamlit run streamlit_ui.py
   ```

3. Open your browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

### Code Execution MCP Server Setup (Optional)

To enable code execution, you need to install Deno and run the MCP server:

1. Install Deno by following the instructions at [https://github.com/denoland/deno/](https://github.com/denoland/deno/)

2. Run the MCP server in a separate terminal:
   ```bash
   deno run -N -R=node_modules -W=node_modules --node-modules-dir=auto jsr:@pydantic/mcp-run-python sse
   ```

3. Uncomment the `mcp_servers=[code_execution_server]` line in `agent.py` to enable code execution 

4. Comment out the other code execution tool

## Troubleshooting

- **Vector Dimensions Mismatch**: Ensure the embedding dimensions in your database match the model you're using. OpenAI models typically use 1536 dimensions, while Ollama's nomic-embed-text uses 768.

- **Function Calling Support**: Not all models support function calling. If using Ollama, make sure to use a model that supports this feature (like Qwen).

- **Database Connection**: For any errors connecting to the database, you can check the logs directly in Supabase. For cloud Supabase, go to "Logs" -> Postgres. For local Supabase, check the logs for the supabase-kong container as well as the supabase-db container.
