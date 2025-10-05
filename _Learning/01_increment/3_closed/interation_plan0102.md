# Increment 1: Core Conversation Loop
## Coding Agent: Gemini 2.5 Pro

## ✅ Setup/Confirm the system prompt for the AI Coding Agent
  see examples/ai-agent-mastery/GOLDEN_RULES.md.  (For me this was creating a GEMINI.md file with the content of the golden rules. I just added "Use uv to install, manage dependencies, and run the application.")

  Confirm with '/memory show'.  You many need to quit and restart Gemini so I picks up all the GEMINI.md files.

## ✅ Create a New Branch
Before you start working on a new feature, bug fix, or experiment, create a new branch from `main`. Give it a descriptive name.

`git checkout main`
`git pull origin main`

Create your new branch and switch to it
`git checkout -b iteration0102`

## Prompt Plan

  ### 2. PLANNING.md
  ✅ `Read @idea.md and @env.example then read and modify the @PLANNING.md document to align with my Increment 1: The Core Conversation Loop of @idea.md . IF you make any assumptions, list them in the ### Assumptions section of the @PLANNING.md document. Explain your modifications.`

  ### 3. TASK.md
  ✅ `Read @idea.md , @.env.example , and @PLANNING.md then read and modify @TASK.md document to align with my Increment 1: The Core Conversation Loop of @idea.md and with @PLANNING.md . Explain your modifications.`

  ### 4. README.md
  ✅ `Read @idea.md , and @env.example , @PLANNING.md , and @TASK.md files, then read and update the @README.md document to align with to align with my Increment 1: The Core Conversation Loop of @idea.md and with @PLANNING.md and @TASK.md . Explain your modifications.`

## Implement

  ### 1. Implement Increment 1
  ✅ Create a Pydantic AI Agent implementing Iteration 1 of @TASK.md while adhere to the following guidelines:
    - follow agent examples from https://ai.pydantic.dev/examples/weather-agent/ and /Users/pmh/code/_new_prj/example_code/ai-agent-mastery/4_Pydantic_AI_Agent/extras/Basic_Pydantic_AI_Agent. Don't follow them to a tee, just use them to get a grasp of and use the Pydantic framework.
    - use .env.example to get an understanding of the necessary environment variables for the agent

## Testing
✅ Unit Test successful
✅ User Tests successful

# Pluck

  # 1. Switch to your main branch (the destination)
  git checkout main
  
  # 2. Pluck the folder and the file from the iteration0102 branch
  git checkout iteration0102 -- _Learning GEMINI.md
  
  # 3. Commit the changes with a clear message
  git commit -m "docs: Pluck learning materials from iteration0102"
  
  # 4. Push the updated main branch to GitHub
  git push
