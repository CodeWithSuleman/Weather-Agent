# Weather-Agent
A lightweight Python-based weather assistant built with the agents library, designed to provide weather information using local context (city and country). This project demonstrates a minimal, context-aware AI agent with a single-tool architecture and basic memory to enhance user interactions.
# Features

- Local Context Handling: Uses a Pydantic LocationContext model to personalize weather responses based on the user's city and country (default: Lahore, Pakistan).

- Simplified Tool: Implements a get_weather tool with string-based arguments to fetch weather data (currently using dummy data for simplicity).

- Minimal Memory: Stores the last query-response pair in a dictionary to enable context-aware responses, such as acknowledging repeated weather queries.

- Greeting Support: Handles greetings like "hello" with friendly, conversational responses.

- Error Handling: Robust try-catch blocks to manage API or tool-related errors gracefully.

- Integrates with the gemini-2.0-flash model via a custom API client for natural language processing.
