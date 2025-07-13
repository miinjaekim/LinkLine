# app/voice_agent/crewai_logic.py

from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


def run_crewai_response(user_input: str) -> str:
    
    load_dotenv()  # This loads variables from .env

    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # or "gemini-1.5-pro" if needed
        google_api_key=api_key,
        temperature=0.7
    )

    voice_agent = Agent(
        role="Research Participant Assistant",
        goal="Speak with potential participants and guide them through the study process",
        backstory=(
            "You're calling people who may be interested in joining a research study. "
            "Your job is to answer questions, sound friendly, and collect basic info if needed."
        ),
        verbose=True,
        llm=llm
    )

    task = Task(
        description=f"The user just said: '{user_input}'. Respond as if you're on a call. Be concise, helpful, and conversational.",
        expected_output="A short sentence spoken out loud by the assistant",
        agent=voice_agent
    )

    crew = Crew(
        agents=[voice_agent],
        tasks=[task],
        verbose=True
    )

    return crew.kickoff()
