"""
main.py – Console entry point.
"""
import bootstrap

import json
import asyncio
from rich import print
from rich.markdown import Markdown

from agents import Runner, SQLiteSession, InputGuardrailTripwireTriggered
from logging_hooks import LoggingHooks
import trip_agents as tg

HOOKS = LoggingHooks()


# ------------------- helpers ------------------------------


def is_profile_complete(profile: tg.TripProfile) -> bool:
    """Check if all required fields in the profile are filled."""
    return all(
        [
            profile.city,
            profile.days,
            profile.budget,
            profile.interests,
            profile.interests_to_avoid,
        ]
    )


async def build_trip(profile: tg.TripProfile):
    """Run the planning and packaging agents."""
    # Construct a detailed prompt that includes all profile aspects
    prompt = (
        f"Plan a {profile.days}-day trip to {profile.city} with a budget of ${profile.budget}. "
        f"The traveler is interested in {', '.join(profile.interests)} "
        f"and wants to avoid {', '.join(profile.interests_to_avoid)}."
    )

    plan_result = await Runner.run(
        tg.planner_agent,
        prompt,
        context=profile.model_dump(),  # Pass full profile as context
        hooks=HOOKS,
    )

    # The planner hands off directly to the packager.
    # The final output of the chain is the markdown trip.
    trip_md = plan_result.final_output.markdown
    print("\n[bold cyan]Your personalized trip:[/bold cyan]\n")
    print(Markdown(trip_md))


# ----------------------- main CLI -------------------------------
async def main():
    session = SQLiteSession("trip_planner_chat")
    print("[bold green]Welcome! I'm your personal trip planner.[/bold green]")
    print("Please tell me about your trip. I need city, dates, budget, and interests.")

    while True:
        # Get user input
        prompt = input("> ").strip()
        if not prompt:
            continue

        try:
            # Run the conversational profile collector
            result = await Runner.run(
                tg.profile_collector_agent, prompt, session=session, hooks=HOOKS
            )
        except InputGuardrailTripwireTriggered:
            print("Input guardrail tripwire triggered.")
            print(f"Please provide relevant information about your trip.")
            continue

        # If agent is done, extract the profile and build the trip
        if result.final_output == "DONE":
            print(
                "\n[bold green]Great! I have all the information I need.[/bold green]"
            )
            print("Now, let's plan your trip...")

            # The conversation is done, now call the extractor agent
            extraction_result = await Runner.run(
                tg.profile_extractor_agent,
                "Extract the user's trip profile from the conversation history.",
                session=session,  # Pass same session to access history
                hooks=HOOKS,
            )
            final_profile = extraction_result.final_output_as(tg.TripProfile)

            if is_profile_complete(final_profile):
                await build_trip(final_profile)
                break
            else:
                print(
                    "[bold red]It seems we're missing some details. Let's try again.[/bold red]"
                )
                session.clear()  # Start over
                continue
        else:
            # Otherwise, print the agent's response and continue the conversation
            print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
