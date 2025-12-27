"""
tools.py – all @function_tool helpers for the demo app.
For the tutorial we keep implementations tiny and deterministic.
"""

from agents import function_tool
import time


# ────────────────────────────────────────────────────────────────
#  Simple FX converter (EURO -> USD) – stub, no live calls
# ────────────────────────────────────────────────────────────────
@function_tool
def currency_convert(
    amount: float, from_currency: str = "EURO", to_currency: str = "USD"
) -> float:
    """Convert EURO to USD using a mocked FX rate."""
    fx_rate = 1.17  # hard-coded for demo
    return round(amount * fx_rate, 2)


# ────────────────────────────────────────────────────────────────
#  web_search – dummy lookup that fabricates search results
# ────────────────────────────────────────────────────────────────
@function_tool
def activity_search(query: str, max_results: int = 5) -> list[dict]:
    """
    Fake web-search tool. Returns a list of {title, url, snippet}.
    In real life you'd call Bing, SerpAPI, Tripadvisor etc.
    """
    time.sleep(0.3)  # simulate latency
    return [
        {
            "title": f"Result {i+1} for {query}",
            "url": f"https://example.com/{i}",
            "snippet": f"Blurb about {query} (#{i+1}).",
        }
        for i in range(max_results)
    ]
