"""
STEP 2 - Native reasoning: let Gemini "think" before it answers.

Gemini 2.5 models can think internally. You control how much with:
  thinking_budget = 0     -> no thinking (fast, cheap)
  thinking_budget = -1    -> dynamic (model decides)
  thinking_budget = 1024  -> up to ~1024 thinking tokens
  include_thoughts=True   -> show a summary of the thinking

Try it: run once with thinking_budget=0, then with 2048, and compare the answers.
Run:  python step2_thinking.py
"""

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini

load_dotenv()

THINKING_BUDGET = 2048  # change this and re-run

agent = Agent(
    model=Gemini(
        id="gemini-2.5-flash",
        thinking_budget=THINKING_BUDGET,
        include_thoughts=True,
    ),
    markdown=True,
)

puzzle = (
    "A shop sells pens at 3 for AED 10. Ali buys 14 pens, but the shop only "
    "sells in packs of 3. How many packs must he buy, how much does he pay, "
    "and how many extra pens does he get?"
)

agent.print_response(puzzle, stream=True)
