from agents import Agent, ModelSettings,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,function_tool, set_tracing_disabled
from agents import enable_verbose_stdout_logging    
import os
from dotenv import load_dotenv

load_dotenv()

enable_verbose_stdout_logging()

set_tracing_disabled(disabled=True)

gemini_api_key=os.getenv("GEMINI_API_KEY")

external_client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

@function_tool

async def math(a:int,b:int):
    a:int=100
    b:int=200
    sum=a+b
    return f"The total value of a and b is {sum} "

booking_agent=Agent(
    name="BookingAgent",
    instructions="You are responsible for booking flight tickets.",
    # tools=[math],
    # (Ya user ki Query ko check krta ha aur according to temperature value answer provide krta ha)
)

start_agent=Agent(
    name="Assitant",
    instructions="You are responsible user query.",
    model="gpt-4o",
    model_settings=ModelSettings(temperature=0.7),

    tools=[math],
    handoffs=[booking_agent],
    # (Ya user ki Query ko check krta ha aur according to temperature value answer provide krta ha)

)
result = Runner.run_sync(
    start_agent,
    # "what is the sum of 100 and 20",
    "hello"
)

print(result.final_output)
print(start_agent.model_settings.to_json_dict())
print(start_agent.model_settings.resolve(override=ModelSettings(temperature=0.5)))
print(start_agent.model_settings.to_json_dict())

