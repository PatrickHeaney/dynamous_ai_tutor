My idea for this project is to create an ai agent that will serve like a tutor, providing guidance and support throughout the ai agent development process.

It will follow the example of https://github.com/dynamous-community/ai-agent-mastery/tree/main/4_Pydantic_AI_Agent

It will have its own:
  - ✅ Supbase Cloud DB
  - local RAG Pipeline

I will use gemini cli 2.5 pro and 2.5 flash as my coding assistant

My v0 version will use openai for text generation and imbedding generation.
 - Use Case 1: local RAG pipeline will include copies of code repositories to be cited as examples
 - Use Case 2: local RAG pipeline will include transcripts of video tutorials.

My v1 version will use a local Ollama LLM for text generation and imbedding generation with a more advanced model.
