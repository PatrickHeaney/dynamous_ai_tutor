# Welcome to the Dynamous AI Tutor Project

  This project is a baseline starting point for creating new AI agents. It begins with the simplest possible runnable agent and will be built upon in future Increments. The goal of this project is for you/me/us to create a comprehensive and user-friendly AI tutor that can assist you in learning how to create AI agents.

  Building this project one increment at a time will help you understand what your AI coding agent is doing and how work together with it to achieve your collective goals.

## My Background

  Back in the 1990's and early 2000's I worked a bit in Fortran 77 as a Mechanical Engineer, but through business school pivoted to project, program, portfolio, and product management. The introduction of generative AI coding assistants, gave new life to my interest in the creativity of creating stuff.

  After creating successful AI workflows in python, I tried to jump to creating AI agents.  I succeeded here and there but really needed to a systematic approach to digest the firehose of advancements and really learn what I was doing so I would create secure and sustainable AI agents. T

# Increments and Iterations:
  To start from the begining, first understand that this project is laid out in **increments and iterations**. Each increment a new feature or a small set of new features.  **Iteration 0** is just is just setting up your development environment, and is one you can reuse to build anything with an AI coding assistant. **Increment 1** just builds the core conversational loop using OpenAI.  Its purpose is to demonstrate and let you practice using our development environment and lets you practice creating the most basic AI agent using the process I am using here.

# Definitions
  **Increment** - a new feature or a small set of new features.
  **Iteration** - an attempt (successful or not) to implement an increment.
  **Branch** - a git/github capability used to create a new branch for a new iteration.
  **Version** - a git/github capability used to create a new Git Tag on the main branch. When you are content with the results of an iteration and after you merge it back to the main branch that you can come back to later. I foresee using these points in the future and starting points for forking off in new directions or adding enhancements.  E.G. Increment 1 currently only includes using OpenAI LLMs, but in the future I will go back and iterate on adding other LLMs as options for the core conversational loop.
  **Fork** - a git/github capability used to create a new repository from an existing one. This is useful for creating a new project based on an existing one. I foresee in the future chosing an appropriate version of this project to fork off from to create very different AI agents.
  **idea.md** - This is the high level idea and increment roadmap for the project. It outlines the overall vision and the planned increments.
  **iteration_plan[][].md** - This is the series of prompts the developer gives to the AI coding agent to understand and implement the desired features in a specific increment.
  **PLANNING.md** - This starts life as examples/ai-agent-mastery/4_Pydantic_AI_Agent/PLANNING.md and is updated by for each increment and iteration by a specific prompt in the `iteration_plan[][].md` file.
  **TASK.md** - This starts life as examples/ai-agent-mastery/4_Pydantic_AI_Agent/TASK.md and is updated by for each increment and iteration by a specific prompt in the `iteration_plan[][].md` file.
  **README.md** - This file.  This started life as examples/ai-agent-mastery/4_Pydantic_AI_Agent/README.md and is updated by for each increment and iteration by a specific prompt in the `iteration_plan[][].md` file.

# Work management
  As an agile manager, I included the simplest imaginable work management tracking system within the _Learning folder.  Within this folder each increment has its own folder and each increment folder has folders for backlog, wip, and closed.  The cornerstone document of each increment is the iteration_plan####.md file. the #### is the to digit increment number follows by the two digit iteration number.  This file contains the purpose, instructions, and prompts, to give the AI coding agent to implment the iteraion.

  After the implementation is complete I ask the AI coding agent to review the implementation and provide feedback on how it could be improved. Here's and example prompt I use for this:

  ```
      The purpose of this request is to enable future developers and ai coding agents to produce new agents and efficiently.  With respect to implementing the AI Agent in {{branch: iteration0205}}, document the issues and how you overcame them, and how future developers and ai coding agents could avoid them.  Use {{example: @_Learning/02_increment/3_closed/lessons_from_0203.md}} as an example and save the new lessons in {{file: @_Learning/02_increment/3_closed/lessons_from_0205.md}}
  ```
  In this case the go in the closed folder because the ai agent has already corrected them.  If AI coding agent did not resolve them, save it to the backlog or WIP folder for the increment.

  I then use these lessons_from files to have the AI Coding Agent create create a new iteration_plan by duplicating and modifying the prior iteration plan to address or avoid the issues identified in the prior lessons_from file(s)

# Instructions:

## Read my idea.md file.
  I will not repeat the outline of increments in this file.

## Increment 0
  Clone this repository and start working on the project. Explore the files and folders to understand the structure of the project.

## Increment 1: The Core Conversation Loop

### Overview
This increment provides the simplest possible, runnable AI agent. It establishes a core conversation loop within a terminal interface, allowing a user to have a basic, stateless conversation with a configurable LLM.

### Setup and Installation (using uv)

1.  **Install uv:**
    If you don't have `uv` installed, you can install it with pip:
    ```bash
    pip install uv
    ```

2.  **Create Virtual Environment & Install Dependencies:**
    From the project's root directory, run `uv sync`. This will create a virtual environment and install all required packages from `requirements.txt`.
    ```bash
    uv sync
    ```

3.  **Configure your Environment:**
    -   Copy the example environment file:
        ```bash
        cp .env.example .env
        ```
    -   Edit the `.env` file with your LLM provider's details. For example:
        -   **For OpenAI:**
            ```
            LLM_BASE_URL=https://api.openai.com/v1
            LLM_API_KEY=sk-your-key-here
            LLM_CHOICE=gpt-4o-mini
            ```
        -   **For a local Ollama instance:**
            ```
            LLM_BASE_URL=http://localhost:11434/v1
            LLM_API_KEY=ollama
            LLM_CHOICE=llama3
            ```

### How to Run
Once the setup is complete, run the agent from your terminal using `uv run`:

```bash
uv run python cli.py
```

This will start the conversational agent. To exit, press `Ctrl+C`.
