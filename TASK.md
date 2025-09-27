# Dynomous AI Agent Mastery Project Tasks

This document outlines the specific implementation tasks for building the MVP of our Dynomous AI Agent, a tutor agent built with Pydantic AI, as described in the `PLANNING.md` file. Tasks are organized by development phase and component.

## Phase 0: Project Setup & Foundation

### Project Initialization
- [x] Create the `dynamous_ai_tutor` directory and initial file structure.
- [x] Create `requirements.txt` and add initial dependencies (Pydantic AI, FastAPI, Streamlit, Supabase client, etc.).
- [x] Create `.env.example` with placeholders for LLM, embedding, Supabase, and web search configurations.

### Supabase Database Setup
- [x] Set up a Supabase project (cloud or local).
- [x] Run SQL scripts to create tables for RAG (documents, document_metadata, document_rows).
- [x] Run SQL scripts to create tables for long-term memory (e.g., user_profiles, conversations, messages).
- [x] Run SQL script to create RPC function for secure SQL queries.

## Phase 1: Core Agent Development (v0 - OpenAI)

### Agent Core (OpenAI)
- [x] Implement the base agent in `agent.py` using Pydantic AI.
- [x] Configure LLM integration with OpenAI for text generation (`LLM_PROVIDER=openai`).
- [x] Configure embedding integration with OpenAI for embedding generation (`EMBEDDING_PROVIDER=openai`).
- [x] Create initial prompt templates in `prompt.py`.
- [x] Implement basic conversation history management.
- [x] Write unit tests for core agent functionality.
- [x] Execute unit tests for core agent functionality.

### Memory System
- [x] Implement short-term conversation memory.
- [x] Implement memory extraction from conversations.
- [x] Create memory vector storage in Supabase.
- [x] Implement memory retrieval system.
- [x] Add memory deduplication mechanism.
- [x] Write unit tests for the memory system.
- [x] Execute unit tests for the memory system.

### Agent Tools
- [x] **Web Search Tool:**
    - [x] Implement web search functionality using Brave API.
    - [x] Write unit tests for web search tools.
- [x] **Document Tools:**
    - [x] Implement a tool to list available documents from the RAG pipeline.
    - [x] Implement a tool to retrieve content of specific documents.
    - [x] Implement a tool to execute read-only SQL queries against tabular data in Supabase.
    - [x] Write unit tests for document tools.

### Terminal User Interface (v0)
- [x] Create `cli_ui.py` for terminal interaction.
- [x] Implement basic input/output for agent interaction.
- [x] Display conversation history in the terminal.

### User Validation for Phase 1
To validate the functionality implemented in Phase 1, follow these steps:

1.  **Environment Setup:**
    * [x]  Ensure you have Python 3.11+ and `uv` installed.
          uv 0.8.5 (ce3728681 2025-08-05)
    * [x]  Clone the repository and navigate to the project root.
    * [x]  Create and activate your virtual environment: `uv venv && source .venv/bin/activate`
    * [x]  Install dependencies: `uv pip install -r requirements.txt`
    * [x]  Copy `.env.example` to `.env` and fill in your `OPENAI_API_KEY`, `BRAVE_API_KEY`, `SUPABASE_URL`, and `SUPABASE_KEY`.
    * [x]  Ensure your Supabase project is set up with the necessary tables (`documents`, `document_metadata`, `document_rows`, `user_profiles`, `conversations`, `messages`) and the `execute_read_only_query` RPC function.

2.  **Run the Terminal UI:**
    *   From the project root, run: `python cli_ui.py`

3.  **Validate Terminal UI and Memory System:**
    *   **Basic Interaction:** Type a simple message like "Hello, agent!" and press Enter. Verify that the agent responds (even with the placeholder message) and that your message and the agent's response appear in the "Conversation History".
    *   **Conversation History Persistence:** Type a few more messages. Observe that the history grows and correctly displays the sequence of interactions.
    *   **Exit:** Type "exit" to quit the application.

4.  **Validate Web Search Tool (Conceptual):**
    *   *Note: The current `cli_ui.py` uses a placeholder agent response. To fully validate the web search tool, you would need to integrate it into the main agent logic (which is part of a later phase). For now, you can conceptually validate its readiness.*
    *   Ensure `BRAVE_API_KEY` is correctly set in `.env`. When the agent is fully integrated, questions requiring external knowledge should trigger web searches.

5.  **Validate Document Tools (Conceptual):**
    *   *Note: Similar to web search, direct interaction with document tools requires agent integration. Conceptual validation involves ensuring setup is correct.*
    *   Ensure `SUPABASE_URL` and `SUPABASE_KEY` are correctly set in `.env`.
    *   If you have documents loaded into your Supabase `documents` and `document_rows` tables, the `list_documents` and `get_document_content` tools are ready to be called by the agent.
    *   If you have the `execute_read_only_query` RPC function set up, the `execute_read_only_sql` tool is ready.

This validation focuses on the foundational components and the basic terminal interaction. Full end-to-end validation of agent tools will occur once the main agent logic is integrated.

## Phase 2: Local RAG Pipeline for Tutor Content

### RAG Pipeline - Common
- [ ] Implement text chunking logic in `RAG_Pipeline/common/text_processor.py`.
- [ ] Develop embedding generation function in `RAG_Pipeline/common/text_processor.py`.
- [ ] Create vector database operations in `RAG_Pipeline/common/db_handler.py` for Supabase.
- [ ] Write unit tests for common RAG components.

### RAG Pipeline - Code Repositories (v0.1)
- [ ] Implement a file watcher in `RAG_Pipeline/Code_Repositories/file_watcher.py` to monitor local code directories.
- [ ] Create `main.py` in `RAG_Pipeline/Code_Repositories` to process code files (e.g., Python, Markdown, etc.).
- [ ] Extract relevant information from code files, chunk, embed, and store in Supabase.
- [ ] Handle updates and deletions of code files.
- [ ] Write unit tests for the code repository RAG pipeline.

### RAG Pipeline - Video Transcripts (v0.2)
- [ ] Implement a file watcher in `RAG_Pipeline/Video_Transcripts/file_watcher.py` to monitor local video transcript directories.
- [ ] Create `main.py` in `RAG_Pipeline/Video_Transcripts` to process video transcript files.
- [ ] Extract text from transcripts, chunk, embed, and store in Supabase.
- [ ] Handle updates and deletions of transcript files.
- [ ] Write unit tests for the video transcript RAG pipeline.

## Phase 3: Transition to Local Ollama (v1)

### Local AI Environment Setup
- [ ] Set up `local-ai-packaged` project (if not already done) to run Ollama and SearXNG locally.
- [ ] Configure Ollama with a suitable advanced LLM and embedding model.

### Agent Configuration Update
- [ ] Update `.env` to use Ollama for LLM (`LLM_PROVIDER=ollama`, `LLM_BASE_URL=http://localhost:11434/v1`).
- [ ] Update `.env` to use Ollama for embedding (`EMBEDDING_PROVIDER=ollama`, `EMBEDDING_BASE_URL=http://localhost:11434/v1`).
- [ ] Adjust vector dimensions in Supabase SQL scripts if the Ollama embedding model requires it.
- [ ] Verify agent functionality with local Ollama models.

## Phase 4: Basic Streamlit User Interface (v1)

### Streamlit UI
- [ ] Create the basic chat interface in `streamlit_ui.py`.
- [ ] Implement session management for conversations.
- [ ] Display chat history in the UI.
- [ ] Add basic styling and layout.
- [ ] Connect the UI to the agent for interaction.
- [ ] Implement error handling and loading indicators in the UI.

## Project Setup & Documentation

### Environment Configuration
- [ ] Ensure `.env.example` is comprehensive and up-to-date.
- [ ] Implement configuration loading and validation within the agent.

### Documentation
- [ ] Complete `README.md` with setup instructions, agent capabilities, and usage examples.
- [ ] Update `PLANNING.md` and `TASKS.md` as development progresses.

### Testing
- [ ] Set up `pytest` configuration for the project.
- [ ] Create test fixtures for common testing scenarios.
- [ ] Implement integration tests for agent-tool interactions.
- [ ] Implement end-to-end tests for the Streamlit UI and agent flow.

## Future Enhancements

### More Tools
- [ ] Implement web search functionality using SearXNG.
- [ ] Add logic to select between Brave and SearXNG based on `.env` configuration.
- [ ] **Code Execution Tool:**
    - [ ] Integrate a code execution tool (e.g., using Deno/MCP server).
    - [ ] Write unit tests for the code execution tool.
- [ ] **Image Analysis Tool:**
    - [ ] Implement image analysis using a vision-capable LLM (e.g., OpenAI's vision models).
    - [ ] Write unit tests for the image analysis tool.

### Advanced RAG
- [ ] **Crawl4AI RAG Server Integration:** Integrate a Crawl4AI RAG Server for processing and storing helpful website content, creating a new RAG pipeline component for web crawling.

### User Interface
- [ ] Develop an advanced React-based frontend with enhanced visualizations and file management, following `5_Agent_Application/` architecture.

### Deployment
- [ ] Implement Docker for containerization of the agent, RAG pipelines, and UI.
- [ ] Explore and implement modular deployment strategies using Docker Compose and cloud platforms (e.g., DigitalOcean, Render, GCP), leveraging `6_Agent_Deployment/`.

### Agent Architecture
- [ ] Explore multi-agent architectures using LangGraph and guardrails (from `7_Agent_Architecture/`) to enhance tutor capabilities and reliability.
- [ ] Add support for additional data sources beyond code repositories and video transcripts.
