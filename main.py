# main.py
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
from connection import config
import asyncio

# Minimal memory: store only the last query-response pair
last_conversation = {"query": "", "response": ""}

# Step 1: Context for location
class LocationContext(BaseModel):
    city: str
    country: str

location = LocationContext(city="Lahore", country="Pakistan")

# Step 2: Simplified tool
@function_tool
def get_weather(city: str, country: str) -> str:
    return f"The weather in {city}, {country} is sunny ☀️ (dummy data)"

# Step 3: Weather agent
weather_agent = Agent(
    name="WeatherAgent",
    instructions="""
You are a weather assistant. For greetings like "hello" or "hi", respond with:
"Hello! I can tell you about the weather in your location. What's up?"

For weather queries (e.g., "What is the weather today?"), use the get_weather tool with the city and country from the context.

If the user asks about the weather and there's a previous weather query in the context, acknowledge it. For example:
"Checking the weather again for Lahore, Pakistan? It's sunny ☀️ (dummy data)."

Example:
Query: "What is the weather today?"
Response: "The weather in Lahore, Pakistan is sunny ☀️"
""",
    tools=[get_weather],
)

# Step 4: Run function
async def main():
    while True:
        query = input("User: ")
        if query.lower() in ["exit", "no", "nothing"]:
            print("Agent: Goodbye! Come back anytime.")
            break
        
        try:
            # Context with location and last conversation
            context = {
                "location": location.model_dump(),
                "last_conversation": last_conversation
            }
            print(f"Context passed to agent: {context}")  # Debug
            
            # Run the agent
            result = await Runner.run(
                weather_agent,
                input=query,
                run_config=config,
                context=context
            )
            final_output = str(result.final_output) if result.final_output else "No response generated."
            print(f"Agent: {final_output}")
            
            # Update minimal memory
            last_conversation["query"] = query
            last_conversation["response"] = final_output
            print(f"Last conversation: {last_conversation}")  # Debug
            
        except Exception as e:
            print(f"Agent: Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())