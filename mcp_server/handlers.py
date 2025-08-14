# 🎯 TEMPLATE INSTRUCTIONS - REMOVE THIS SECTION WHEN IMPLEMENTING YOUR MCP SERVER
"""
HANDLERS.PY TEMPLATE GUIDE:

📋 WHAT TO REPLACE:
1. Remove ALL weather API imports (httpx, dotenv) if you don't need them
2. Remove ALL weather API functions (lines marked as "WEATHER EXAMPLE")
3. Remove WEATHER_API_KEY and weather-specific environment loading
4. Replace with YOUR actual tool implementations
5. Update TOOL_FUNCTIONS mapping at the bottom with your tools

📝 WHAT TO KEEP:
- The basic structure and error handling patterns
- The TOOL_FUNCTIONS dictionary pattern (just change the content)
- Async function patterns for your tools
- Input validation examples

⚠️ CRITICAL:
- All tool functions MUST be async
- All tool functions MUST match the schemas in tools.json
- All tool functions MUST handle errors gracefully
- Return values MUST match your outputSchema exactly

📚 EXAMPLE PATTERNS TO COPY:
- Input validation: Check required parameters first
- Error handling: Use try/catch with meaningful error messages
- Return format: Always return dict matching your outputSchema
- Type hints: Use proper Python type annotations
"""

# ============================================================================
# 🔧 YOUR IMPORTS SECTION - Replace these with your actual dependencies
# ============================================================================
# TODO: Replace weather API imports with your actual imports
# Examples:
# import requests          # For HTTP requests
# import json             # For JSON handling
# import sqlite3          # For database access
# from your_library import YourClass  # Your specific libraries

# WEATHER EXAMPLE IMPORTS - REMOVE THESE!
import os
from datetime import datetime
import httpx
from dotenv import load_dotenv

# ============================================================================
# 🔑 YOUR ENVIRONMENT SETUP - Replace with your actual config
# ============================================================================
# TODO: Replace with your actual environment variable loading
# Examples:
# YOUR_API_KEY = os.getenv("YOUR_API_KEY")
# DATABASE_URL = os.getenv("DATABASE_URL")
# CONFIG_VALUE = os.getenv("CONFIG_VALUE", "default_value")

# WEATHER EXAMPLE CONFIG - REMOVE THIS!
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


# ============================================================================
# 🛠️ YOUR UTILITY FUNCTIONS - Replace with your actual helper functions
# ============================================================================
# TODO: Add your utility functions here
# Examples:
# def validate_email(email: str) -> bool:
#     return "@" in email and "." in email
#
# def format_response(data: dict) -> dict:
#     return {"status": "success", "data": data}
#
# async def your_async_helper(param: str) -> str:
#     # Your async processing
#     return processed_result


# WEATHER EXAMPLE UTILITY - REMOVE THIS!
def validate_date(dt_str: str) -> None:
    """Example utility function - shows input validation pattern."""
    try:
        datetime.strptime(dt_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date: {dt_str}. Use YYYY-MM-DD.")


# WEATHER EXAMPLE FUNCTION - REMOVE THIS!
async def fetch(endpoint: str, params: dict) -> dict:
    """Example HTTP client function - shows API call patterns with error handling."""
    if not WEATHER_API_KEY:
        raise ValueError("Weather API key not set.")

    params["key"] = WEATHER_API_KEY
    url = f"https://api.weatherapi.com/v1/{endpoint}"
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, params=params)
            try:
                data = resp.json()
            except Exception:
                data = None
            if resp.status_code != 200:
                detail = (data or {}).get("error", {}).get("message", resp.text)
                raise ValueError(f"WeatherAPI error: {detail}")
            return data
        except httpx.RequestError as e:
            raise ValueError(f"Request error: {e}")
        except Exception as e:
            raise ValueError(f"Unexpected error: {e}")


# ============================================================================
# 🛠️ YOUR TOOL FUNCTIONS - Replace ALL weather functions with your actual tools
# ============================================================================
# TODO: Replace all weather functions below with YOUR actual tool implementations
# Each function must:
# 1. Be async
# 2. Match the inputSchema from tools.json exactly
# 3. Return dict matching outputSchema from tools.json exactly
# 4. Handle errors gracefully with proper error messages
# 5. Include type hints for parameters and return value

"""
TEMPLATE PATTERNS FOR YOUR TOOLS:

# Simple tool example:
async def your_simple_tool(text: str, count: int = 10) -> dict:
    \"\"\"Your tool description.\"\"\"
    # 1. Validate inputs
    if not text:
        raise ValueError("text parameter is required")
    if count < 1 or count > 100:
        raise ValueError("count must be between 1 and 100")
    
    # 2. Process request
    result = process_your_data(text, count)
    
    # 3. Return response matching outputSchema
    return {
        "result": result,
        "success": True,
        "metadata": {"count": count}
    }

# Complex tool with API calls:
async def your_api_tool(query: str, options: dict = None) -> dict:
    \"\"\"Your API tool description.\"\"\"
    try:
        # Input validation
        if not query:
            raise ValueError("query is required")
        
        # API call with error handling
        response = await make_api_call(query, options)
        
        # Process and return
        return {
            "data": response,
            "status": "success"
        }
    except Exception as e:
        raise ValueError(f"API error: {e}")
"""

# 🌤️ WEATHER EXAMPLE FUNCTIONS - REMOVE ALL OF THESE!
# The following functions are examples showing different patterns:


# WEATHER EXAMPLE - Simple function with validation
async def get_current_weather(query: str, include_air_quality: bool = False) -> dict:
    if not query:
        raise ValueError("query with location is required.")
    return await fetch(
        "current.json", {"q": query, "aqi": "yes" if include_air_quality else "no"}
    )


# WEATHER EXAMPLE - Complex function with multiple parameters and validation
async def get_weather_forecast(
    query: str,
    days: int = 1,
    include_air_quality: bool = False,
    include_alerts: bool = False,
) -> dict:
    if not query:
        raise ValueError("query with location is required.")
    # Free plan only allows 3 days of forecast
    if days < 1 or days > 3:
        raise ValueError("'days' must be between 1 and 3.")
    return await fetch(
        "forecast.json",
        {
            "q": query,
            "days": days,
            "aqi": "yes" if include_air_quality else "no",
            "alerts": "yes" if include_alerts else "no",
        },
    )


# WEATHER EXAMPLE - Simple function with single parameter and array output


async def search_locations(query: str) -> dict:
    if not query:
        raise ValueError("query with location is required.")
    locations = await fetch("search.json", {"q": query})
    return {"items": locations}


# ============================================================================
# 🔗 TOOL FUNCTIONS MAPPING - Update this with your actual tools
# ============================================================================
# TODO: Replace with your actual tool mappings
# This dictionary maps tool names (from tools.json) to their implementation functions
#
# YOUR MAPPING SHOULD LOOK LIKE:
# TOOL_FUNCTIONS = {
#     "your_tool_name": your_tool_function,
#     "another_tool": another_tool_function,
#     "ping": simple_ping_tool,
# }

# WEATHER EXAMPLE MAPPING - REMOVE THIS! (Only 2 tools kept as examples)
TOOL_FUNCTIONS = {
    "get_weather": get_weather_forecast,
    "search_locations": search_locations,
}
