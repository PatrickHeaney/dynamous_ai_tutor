Use @docs:pydantic-docs and search the web for the Brave and SearXNG API documentation to create a Pydantic AI agent that has the ability to search the web with either Brave or SearXNG.

Here is what the .env.example file should look like, which you will generate and also use to get an understanding of the necessary environment variables for the agent:


# Set this to either openai, openrouter, or ollama
LLM_PROVIDER=

# Base URL for the OpenAI compatible instance
LLM_BASE_URL=

# API key for OpenAI or OpenRouter (no need to set for Ollama)
LLM_API_KEY=

# The LLM you want to use for the agents.
LLM_CHOICE=

# Set your Brave API key if using Brave for agent web search (leave empty if using SearXNG)
BRAVE_API_KEY=

# Set the SearXNG endpoint if using SearXNG for agent web search (leave empty if using Brave)
SEARXNG_BASE_URL=

So you will create one function to search with Brave, and another to search with SearXNG. Which environment variable is set will determine which function the agent uses for its web search tool.

Use the following agent example from the Pydantic AI documentation to aid in your agent creation. Don't follow this to a tea, just use it to get a grasp on the framework:

https://ai.pydantic.dev/examples/weather-agent/

After creating the MCP server with FastMCP, update README.md and TASK.md since you now have the initial implementation for the server.
