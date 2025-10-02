# from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled
# import os
# from dotenv import load_dotenv

# load_dotenv()
# set_tracing_disabled=True

# gemini_api_key=os.getenv("OPENAI_API_KEY")
# external_client=AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#     )

# model = OpenAIChatCompletionsModel(
#     model="gpt-4o",
#     openai_client=external_client
#     )
# biology_agent=Agent(
#     name="Bio_Assistant",
#     instructions="You are specilized for biology assistant for solving biology problem",
# )
# geography_agent=Agent(
#     name="Geo_Assistant",
#     instructions="You are specilized for geography assistant for solving geography problem",
# )
# mathematics_agent= Agent(
#     name="Math_Assistant",
#     instructions="You are specilized for mahtematic assistant for solving math problem",
#     )
# main_agent= Agent(
#     name="Orchestrator",
#     instructions="YOU ARE SPECILIZED FOR HANDLING ALL THE TASKS",
#     handoffs =[biology_agent,geography_agent,mathematics_agent],
#     )


# result = Runner.run_sync(
#     main_agent,
#         """What is the answer to 2000+1258-457 = ?
#         tell me about pakistan ?
#         WHAT IS the role of heart in our body?
#         """,
#     )
# print(result.final_output)



### Chainlit work 


# from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled
# import main as cl
# import os
# from openai.types.responses import ResponseTextDeltaEvent
# from dotenv import load_dotenv

# load_dotenv()
# set_tracing_disabled=True

# gemini_api_key=os.getenv("GEMINI_API_KEY")

# external_client=AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",    
#     )
# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
#     )
    
# @cl.on_chat_start
# async def handle_chat_start():
#     cl.user_session.set("history",[ ])
#     await cl.Message(content="friday_slot")
# @cl.on_message
# async def handle_message(message:cl.Message):
#     history=cl.user_session.get("history")
#     history.append({"role":"user","content":message.content})
#     msg= cl.Message(content=" ")
#     await msg.send()
    
#     result = await Runner.run(main_agent,input=message.content)
#     await cl.Message(content=result.final_output).send()

# biology_agent=Agent(
#     name="Bio_Assistant",
#     instructions="You are specilized for biology assistant for solving biology problem",
# )
# geography_agent=Agent(
#     name="Geo_Assistant",
#     instructions="You are specilized for geography assistant for solving geography problem",
# )
# mathematics_agent= Agent(
#     name="Math_Assistant",
#     instructions="You are specilized for mahtematic assistant for solving math problem",
#     )
# main_agent= Agent(
#     name="Orchestrator",
#     instructions="YOU ARE SPECILIZED FOR HANDLING ALL THE TASKS",
#     handoffs =[biology_agent,geography_agent,mathematics_agent],
#     )
# result = Runner.run_sync(
#     main_agent,
#         """What is the answer to 2000+1258-457 = ?
#         """,
#     )
# print(result.final_output)

#### Basic Preparation for Agent sdk exame 

from agents import Agent,Runner,set_tracing_disabled,enable_verbose_stdout_logging,RunContextWrapper
import os
from dotenv import load_dotenv

load_dotenv()
enable_verbose_stdout_logging()

set_tracing_disabled=True
# ab agr mujy koy be file ma jana ho to mujy ctrl press+cursor+like agent ma jana ha to uspy jaky click krngay to hamin agent ki file ka sara code show kree gaa
# ya process sub k liya same hogaa

def system_prompt(ctx: RunContextWrapper, agent: Agent):
    # TypeError: system_prompt() missing 2 required positional arguments: 'ctx' and 'agent'
    # ya error pass krta ha jab ham ctx aur agent ki type define nae krty hain to 
    return "what is 14=28/2 "


agent=Agent(
    # name=22552,
    #  (again same error throw kree gaa)
    # name=12354,agr ham name ma str k alawa second form daty hain aur tracing true ho to ya error show kree gaa 
    # (raise TypeError(f"Agent name must be a string, got {type(self.name).__name__}"))
    name="Mathematic",
    # instructions="You are specilized for checkup patient query and suggest medicine. "
    instructions=system_prompt   
    )
result=Runner.run_sync(
    agent,
#    input= """What is the medicine for fever and headache?which medicine is usefull for fungel skin """,
    'hi'
    )      
print(result.final_output)

