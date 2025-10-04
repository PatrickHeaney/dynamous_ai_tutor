My idea for this project is to create baseline starting point for new AI agents.

## Incremental Learning and Development Plan

The project will follow an incremental and iterative development model. Each Increment delivers a runnable, testable version of the agent with increasing capabilities, ensuring continuous feedback and progress. Each iteration is a turn practicing implementation of the increment. I encourage you to experiment over multiple iterations and learning and trying new things.  The point is to provide you confidence in your ability to build this increment, or a fork of, this increment.

My intent is to create branch for each Increment then others can use this as a lesson plan to gradually learn and build their own AI assistant development process.

I can then go back and merge changes from previous Increments into the main branch and have a robust new starting point for future Increments.

### Increment 1: [] The Core Conversation Loop
*   **Goal**: Create the simplest possible, runnable agent.
*   **Functionality**: A user can start the terminal UI, have a basic conversation with the agent (no tools, no memory), and the agent will respond using the LLM.
*   **Testing**: Unit and user tests for agent/UI initialization to to validate.

### Increment 2: [] Adding Memory
*   **Goal**: Make the agent stateful and conversational.
*   **Functionality**: The agent can remember information from earlier in the same conversation **and recall it in subsequent conversations after an application restart.**
*   **Testing**:
  * Unit tests for the `mem0` integration points. User testing by asking the agent to recall previously mentioned facts.
  * Integration tests for the `mem0` integration points. User testing by asking the agent to recall previously mentioned facts.

### Increment 3: [] Adding Web Search
*   **Goal**: Give the agent its first tool to access external knowledge.
*   **Functionality**: The agent can answer questions about recent events or topics outside its training data.
*   **Testing**: Unit tests for the web search tool. User testing to confirm the agent uses the tool correctly.

### Increment 4: [] Adding RAG

### Increment 5: [] Adding MCP Servers

### Increment 6: [] Adding Crawl4AI 

My list of Local MCP Servers includes
[] Brave Search - `https://github.com/brave/brave-search-mcp-server`
[] Manage local files - `https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem`
[] Manage local git repositories - `https://github.com/modelcontextprotocol/servers/tree/main/src/git`
[] Crawl4AI RAG - `https://github.com/coleam00/mcp-crawl4ai-rag`