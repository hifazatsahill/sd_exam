from agents import Agent,Runner
from dotenv import load_dotenv

load_dotenv()

from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, function_tool,enable_verbose_stdout_logging
import os
from dotenv import load_dotenv
import requests
import random



load_dotenv()
# set_tracing_disabled(disabled=True)

enable_verbose_stdout_logging()

gemini_api_key = os.getenv("GEMINI_API_KEY")


provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gpt-4o",
    openai_client=provider
)


@function_tool
def add_number(a:int,b:int =10) -> str:

    """
    Get Random Number

    Args:
        a:first
        b:secound
    """
    return random.randint(1, 10)

@function_tool
def get_weather(city: str) -> str:
    """
    Get the weather for a given city"""

    try:
        result = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key=8e3aca2b91dc4342a1162608252604&q={city}"
        )

        data = result.json()

        return f"The current weather in {city} is {data['current']['temp_c']}C with {data['current']['condition']['text']}."

    except Exception as e :
        return f"Could not fetch weather data due to {e}"
main_agent=Agent(
    name='assistant',
    instructions="You are hepfull assistant to resolve user query ",
    tools=[get_weather,add_number]
)

result=Runner.run_sync(
    main_agent,
    'Hello tell me about the karachi weather ?'
)
print(result.final_output)