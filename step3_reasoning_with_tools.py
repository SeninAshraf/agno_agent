"""
STEP 3 - Reasoning WITH tools: a mini market-research analyst.

This is the "Reasoning with Tools" idea from the Agno docs:
put ReasoningTools (think + analyze) next to a real tool (web search)
on ONE agent. The agent then loops:

    think()   -> plan what to search
    search    -> get real results from the web
    analyze() -> are the results good enough? if not, search again
    answer    -> write the final brief

Run:  python step3_reasoning_with_tools.py
Then change TOPIC to anything you're curious about.
"""

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.websearch import WebSearchTools

load_dotenv()

TOPIC = "the food delivery app market in the UAE"

analyst = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    tools=[
        ReasoningTools(add_instructions=True),  # gives the agent think() and analyze()
        WebSearchTools(),                       # gives the agent a web search tool
    ],
    instructions=[
        "You are a junior business analyst.",
        "Always plan with think() before searching, and check results with analyze().",
        "Write a short brief with these sections: Key Players, Customer Needs, "
        "Opportunities, Risks, Sources.",
        "Only state facts you found in search results, and list their URLs under Sources.",
    ],
    markdown=True,
)

analyst.print_response(
    f"Research {TOPIC} and write a one-page brief.",
    stream=True,
    show_full_reasoning=True,  # prints the think/analyze steps so you can watch them
)
