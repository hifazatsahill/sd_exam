from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel, function_tool 
from agents import set_tracing_disabled,enable_verbose_stdout_logging
import os
from dotenv import load_dotenv
load_dotenv()
set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()

@function_tool
def helper_book(a:int,b:int):
    sum=a+b
    return f"The sum of {a} and {b} is {sum}"


# city= "karachi"
# @function_tool
# def get_weather(city: str) -> str:
#     """returns weather info for the specified city."""
#     return f"The weather in {city} is sunny"

nextJs_agent=Agent(
    name="Assistant",
    instructions="You are specilized for next js work and solve problem codantic ."

)
agent = Agent(
    name="Haiku agent",
    instructions="Always respond in haiku form",
    handoffs=[nextJs_agent],
    tools=[helper_book]
)
result = Runner.run_sync(agent,
    """what is the weather in Karachi?,what is next js used for? """,max_turns=2)

print(result.final_output)