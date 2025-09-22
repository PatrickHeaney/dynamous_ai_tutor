# Dynomous AI Agent Mastery Project Tasks

This document outlines the specific implementation tasks for building the MVP of our Dynomous AI Agent, a tutor agent built with Pydantic AI, as described in the `PLANNING.md` file. Tasks are organized by development phase and component.

## Phase 0: Project Setup & Foundation

### Project Initialization
- [x] Create the `dynomous_ai_agent` directory and initial file structure.
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
- [ ] Execute unit tests for the memory system. (Blocked by environment issue)
- [ ] Execute unit tests for the memory system.

### Agent Tools
- [ ] **Web Search Tool:**
    - [ ] Implement web search functionality using Brave API.
    - [ ] Implement web search functionality using SearXNG.
    - [ ] Add logic to select between Brave and SearXNG based on `.env` configuration.
    - [ ] Write unit tests for web search tools.
- [ ] **Code Execution Tool:**
    - [ ] Integrate a code execution tool (e.g., using Deno/MCP server).
    - [ ] Write unit tests for the code execution tool.
- [ ] **Image Analysis Tool:**
    - [ ] Implement image analysis using a vision-capable LLM (e.g., OpenAI's vision models).
    - [ ] Write unit tests for the image analysis tool.
- [ ] **Document Tools:**
    - [ ] Implement a tool to list available documents from the RAG pipeline.
    - [ ] Implement a tool to retrieve content of specific documents.
    - [ ] Implement a tool to execute read-only SQL queries against tabular data in Supabase.
    - [ ] Write unit tests for document tools.

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

## Phase 4: Basic User Interface

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
