# Experiment 11: LCEL Story Generation

## Aim
To build a simple LangChain Expression Language (LCEL) chain that generates short stories based on user-provided topics using OpenAI GPT-3.5-turbo.

## Problem Statement
Create an LCEL chain using a prompt template, an LLM, and an output parser. Invoke the chain with at least two hardcoded topics and print the generated stories.

## Technologies Used
- Python
- LangChain
- LangChain OpenAI
- OpenAI GPT-3.5-turbo

## Algorithm
1. Install the required packages.
2. Set the OpenAI API key as an environment variable.
3. Import `ChatPromptTemplate`, `ChatOpenAI`, and `StrOutputParser`.
4. Define a prompt template containing `{topic}`.
5. Initialize the GPT-3.5-turbo model.
6. Create the chain using `prompt | llm | parser`.
7. Invoke the chain for two different topics.
8. Print the generated stories.

## Installation

```bash
pip install -r requirements.txt
```

## API Key Setup

**Windows Command Prompt:**

```cmd
set OPENAI_API_KEY=your_api_key_here
```

**Windows PowerShell:**

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

Replace the placeholder with your own API key. Never upload your API key to GitHub.

## Execution

```bash
python src/main.py
```

## Expected Output

The stories are generated dynamically, so the exact text may vary.

```text
Topic: a dragon and a knight
Story: A brave knight met a dragon guarding a hidden cave.
Instead of fighting, they joined forces to protect a
magical kingdom.

Topic: a lost spaceship
Story: A spaceship drifted through a distant galaxy.
A mysterious signal guided its crew toward a forgotten
planet full of life.
```

## Result
The LCEL chain was designed using the pipe syntax `prompt | llm | parser` to generate short stories for multiple topics and return the output as strings.
