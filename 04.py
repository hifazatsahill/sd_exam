from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,function_tool,handoff
from agents import set_tracing_disabled,enable_verbose_stdout_logging
import os
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"), 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
    )

@function_tool
def helper_book(a:int,b:int):
    sum=a+b
    return f"The sum of {a} and {b} is {sum} ."


user ="mathematic"

def user_input():
    if user =="mathematic":
        return True
    else :
        return f"Yar ya  mara range ma nae ha isliya ye sawal nae kar sakta ."


math_agent=Agent(
    name="MathChecker",
    instructions="You are a math expert. You can only answer math questions.",
    handoff_description="you specilized math query and solve question .",
)
python_agent=Agent(
    name="PythonAgent",
    instructions="You are a python expert. You can only answer python questions.",
    handoff_description="you specilized python query and solve question .",
)
triage_agent = Agent(
    name="triage_agent",
    instructions="You are a triage expert. You delegate tasks to the appropriate agents or tools.",
    tools=[helper_book],
    handoffs=[math_agent, python_agent],
)
result = Runner.run_sync(
    triage_agent,
    """ what is the sum of 45 and 78?,what is 56 plus 89? what is the python language ? """,
)

print(result.final_output)
