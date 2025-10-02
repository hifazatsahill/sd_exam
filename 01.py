from agents import Agent,Runner,set_tracing_disabled,enable_verbose_stdout_logging,RunContextWrapper
import os
from dotenv import load_dotenv

load_dotenv()
enable_verbose_stdout_logging()

set_tracing_disabled=True
# gemini_api_key=os.getenv("GEMINI_API_KEY")

# def system_prompt(ctx: RunContextWrapper, agent: Agent):
#     return "what is 14=28/2 "
user='math'

agent=Agent(
    name="Mathematic",
    # Yhan pa instruction ki jagah jo system prompt darhy thea uski jagah prompt pass kr k 
    # openai.plateform ma jaky chat create chate prompt kr kay ham uski id aur version pas kr ka be run kr sakyhain
    prompt={
        "id": "pmpt_68cbad46845c819597615e08072b4da80f2f873b9e141512",
        "version": "3",
        "variables": {
    "topic": user
    }
    }
    # prompt={
    #     "id": "pmpt_68cbad46845c819597615e08072b4da80f2f873b9e141512",
    #     # ya version 2 isliya aya ha ki many prompt ko update kiya tha
    #     "version": "2"
    # },
    )
result=Runner.run_sync(
    agent,
    input='(a+b)2 define it'
    )      
print(result.final_output)
