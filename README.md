# Agno + Gemini Starter

Three tiny scripts that take you from "hello" to a reasoning agent that uses tools.

| Script | What you learn |
|---|---|
| `step1_hello_agent.py` | What an agent is: model + instructions |
| `step2_thinking.py` | Native reasoning: Gemini's `thinking_budget` |
| `step3_reasoning_with_tools.py` | ReasoningTools + web search: think → search → analyze → answer |

## Setup (one time)

1. Install Python 3.10 or newer.
2. Get a free Gemini API key at https://aistudio.google.com/apikey
3. In this folder, run:

```bash
python -m venv .venv
# Windows:   .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and paste your key into it.
   Never share or upload your `.env` file.

## Run

```bash
python step1_hello_agent.py
python step2_thinking.py
python step3_reasoning_with_tools.py
```

## Practice ideas

- Step 2: set `THINKING_BUDGET = 0`, then `4096`. Does the answer change?
- Step 3: change `TOPIC` to a company or industry you'd like to work in.
- Step 3: remove `ReasoningTools(...)` from the tools list and compare the output.

## Common errors

- `API key not valid` / `401` → check `.env` has `GOOGLE_API_KEY=...` with no quotes or spaces.
- `429` / quota exceeded → free-tier limit hit; wait a minute and retry.
- `ModuleNotFoundError: agno.tools.websearch` → run `pip install -U agno`.
- Model not found → try `id="gemini-2.5-flash-lite"` or check model names in Google AI Studio.
