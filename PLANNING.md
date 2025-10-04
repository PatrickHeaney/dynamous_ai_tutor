# Pydantic AI Web Search Agent - Project Planning

## Project Overview
This project aims to build a Pydantic AI agent capable of searching the web using either Brave Search API or SearXNG, depending on environment configuration. The agent will be versatile, allowing for seamless switching between search providers while maintaining consistent functionality and response structure.

## Architecture

### Components
1. **Agent Core (agent.py)**
   - Main Pydantic AI agent implementation
   - Handles system prompt and tool integration
   - Manages environment-based configuration

2. **Search Tools (tools.py)**
   - Brave Search implementation
   - SearXNG implementation
   - Common interface for both search providers

3. **System prompt (prompt.py)**
   - Main prompt for the AI agent

### Tech Stack
- **Pydantic AI**: Core agent framework
- **Python 3.10+**: Base language
- **httpx**: For async HTTP calls
- **python-dotenv**: For environment variable management
- **pytest**: For unit testing

## Search Provider Integration

### Brave Search
- **API Endpoint**: https://api.search.brave.com/res/v1/web/search
- **Authentication**: API key via `X-Subscription-Token` header
- **Query Parameters**: q (query), count (results), country, etc.
- **Key Features**: Web search, news, videos, images
- **Configuration**: BRAVE_API_KEY environment variable

### SearXNG
- **API Endpoint**: Self-hosted or public instance (via SEARXNG_BASE_URL)
- **Authentication**: None required (for most instances)
- **Query Parameters**: q (query), categories, engines, etc.
- **Key Features**: Metasearch capabilities, privacy-focused
- **Configuration**: SEARXNG_BASE_URL environment variable

## System Prompt Strategy
The agent will use a dynamic system prompt that:
1. Explains its capability to search the web
2. Indicates which search provider is being used
3. Provides relevant disclaimers about search results
4. Includes instructions on how to format and present search results

## Agent Functionality

### Primary Features
- Web search with query customization
- Configurable number of results
- Consistent response formatting
- Error handling and rate limit management
- Automatic provider selection based on environment

### Agent Input/Output Structure
- **Input**: Natural language queries
- **Output**: Structured search results with:
  - Title
  - URL
  - Snippet/description
  - Source attribution

## Testing Strategy
- Test each agent tool for web search
- Mock responses for reliable testing
- Error condition testing