"""
trip_agents.py – all Agent objects & output schemas.
"""

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field

from agents import (
    Agent,
    InputGuardrail,
    GuardrailFunctionOutput,
    RunContextWrapper,
    Runner,
)

# from tools import activity_search


# ────────────────────────────────────────────────────────────────
# 1) Safety guardrail (checks every user message)
# ────────────────────────────────────────────────────────────────


class SafetyCheckOut(BaseModel):
    is_safe_and_relavant: bool = Field(..., description="True if the input is allowed.")
    reasoning: str


safety_guard_agent = Agent(
    name="Safety guardrail",
    instructions=(
        "If the user text contains harassment, hate speech, illegal requests, or anything not related to travel planning, "
        "set is_safe_and_relavant = False and explain briefly in reasoning. Otherwise is_safe_and_relavant = True."
    ),
    output_type=SafetyCheckOut,
    model="o3-mini",
)


async def safety_guardrail(
    ctx: RunContextWrapper, agent: Agent, input_data: str
) -> GuardrailFunctionOutput:
    """Check for safe, allowed input."""
    result = await Runner.run(safety_guard_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(SafetyCheckOut)
    return GuardrailFunctionOutput(
        output_info=final_output.reasoning,
        tripwire_triggered=not final_output.is_safe_and_relavant,
    )


# ────────────────────────────────────────────────────────────────
# 2) Profile collector (conversational)
# ────────────────────────────────────────────────────────────────


profile_collector_agent = Agent(
    name="Profile collector",
    instructions=(
        "You are a friendly and helpful travel assistant.\n"
        "Your goal is to collect a complete travel profile from the user by asking questions.\n"
        "Ask questions ONE AT A TIME until all of the following fields are known:\n"
        "- Destination city\n"
        "- Trip length in days\n"
        "- Total budget in USD\n"
        "- Interests (activities, food, etc.) and interests to avoid\n"
        "Once all information is gathered, respond with ONLY the word 'DONE'."
    ),
    input_guardrails=[InputGuardrail(guardrail_function=safety_guardrail)],
    model="o3-mini",
)


# ────────────────────────────────────────────────────────────────
# 3) Profile extractor
# ────────────────────────────────────────────────────────────────


class TripProfile(BaseModel):
    city: Optional[str] = None
    days: Optional[int] = None
    budget: Optional[float] = None
    interests: Optional[List[str]] = None
    interests_to_avoid: Optional[List[str]] = None


profile_extractor_agent = Agent(
    name="Profile extractor",
    instructions=(
        "You are an expert data extraction agent.\n"
        "A user has had a conversation with a travel assistant.\n"
        "Read the conversation history and extract the final, consolidated details into a `TripProfile` object.\n"
        "Ensure all fields are filled."
    ),
    output_type=TripProfile,
    model="o3-mini",
)


# ────────────────────────────────────────────────────────────────
# 4) Day-packager
# ────────────────────────────────────────────────────────────────
class TripOut(BaseModel):
    markdown: str


packager_agent = Agent(
    name="Day packager",
    instructions=(
        "Turn the activity list into a day-by-day markdown trip with headings, times, "
        "bullet-points, and emoji. Split activities evenly across the number of days from the user's profile.\n"
        "Include total cost in USD at the bottom."
    ),
    output_type=TripOut,
    model="o3-mini",
)


# ────────────────────────────────────────────────────────────────
# 5) Planner agent
# ────────────────────────────────────────────────────────────────
class PlanItem(BaseModel):
    title: str
    price_usd: float
    why: str


class PlannerOut(BaseModel):
    items: List[PlanItem]


planner_agent = Agent(
    name="Activity planner",
    instructions=(
        "You are an expert travel planner creating a list of activities. The user's complete trip profile is in the context.\n"
        "You MUST create a plan that reflects the user's `interests`.\n"
        "You MUST NOT include any activities related to the user's `interests_to_avoid`.\n"
        "The total cost of all activities must not exceed the provided budget.\n"
        "Once the activity list is ready, HANDOFF to the Day packager agent.\n"
        # "- You may call activity_search for live ideas."
    ),
    output_type=PlannerOut,
    model="o3-mini",
    # tools=[activity_search],
    handoffs=[packager_agent],
)
