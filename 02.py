from agents import Agent,Runner,set_tracing_disabled,enable_verbose_stdout_logging,RunContextWrapper
import os
from dotenv import load_dotenv

load_dotenv()
enable_verbose_stdout_logging()

set_tracing_disabled=True

# user='math'

math_agent=Agent(
    name="Mathematic",
    instructions="you are specilized to answer math related questions",
#     prompt={
#         "id": "pmpt_68cbad46845c819597615e08072b4da80f2f873b9e141512",
#         "version": "3",
#         "variables": {
#     "topic": user
#     }
# }
    )
visa_agent=Agent(
    name="Visa",
    instructions="you are specilized to answer visa related questions",
)
triage_agent=Agent(
    name="Triage",
    instructions="you are specilized to check the user query and decide which agent to use",
    handoffs=[math_agent,visa_agent],
handoff_description="if the user query is related to math, handoff to Mathematic agent, otherwise respond yourself",
)

result=Runner.run_sync(
    triage_agent,
    'Hello, I want to apply for a US visa. Can you help me with the process?'
    'how i can relife my stress?'
    )      
print(result.final_output)
