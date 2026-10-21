"""
STEP 1 - Your first Agno agent, powered by Gemini.

Goal: check that your API key works and see what an "agent" looks like.
Run:  python step1_hello_agent.py
"""

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini

load_dotenv()  # reads GOOGLE_API_KEY from your .env file

# An Agent = a model (the brain) + instructions (the job description)
agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    instructions="You are a friendly tutor. Explain things simply, in under 100 words.",
    markdown=True,
)

agent.print_response("What is a Business Analyst, in one short paragraph?", stream=True)
