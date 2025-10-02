## Basic To Advance Concept in AI SDK
### folder open and then write there (C:\Windows\System32\cmd.exe)-->. select this folder and write " CMD "
* basic command use on powershell
    * 
    * uv init --("yahan pa wo name likhngay jispy project open krnay ha)
    * open vscode for use command " code ."
    * UV ADD OPENAI-AGENTS PYTHON-DOTENV
    *  AB ya packege .venv file ms store hota ha
    * uv venv (Ya VU environment ki command ha)
    * (.venv\Scripts\activate) ya command show hoge usko copy kr k next line ma (ctl+v) kr kay paste krngy aur run karngy
 # Basic Agent Code 

 """ from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled
import os
from dotenv import load_dotenv

load_dotenv()

set_tracing_disabled=True

api_key=os.getenv("OPENAI_API_KEY")

external_client=AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
model = OpenAIChatCompletionsModel( 
    model="gpt-4o",
    openai_client=external_client
    )
agent=Agent(
    name="Doctor",
    instructions="You are specilized for checkup patient query and suggest medicine. "
)

result= Runner.run_sync(
    agent,
    """What is the medicine for fever and headache?
    """,
    model=model
)   
print(result.final_output)
 """

## Jab HUM OPENAI_API_KEY KA SAT KAM KRNGY TO BASIC SAMPLE AGENT AK PROJECT HA 
* from agents import Agent,Runner,set_tracing_disabled
import os
from dotenv import load_dotenv

load_dotenv()

set_tracing_disabled=True

agent=Agent(
    name="Doctor",
    instructions="You are specilized for checkup patient query and suggest medicine. "
    )

result=Runner.run_sync(
    agent,
    "What is the medicine for fever and headache? ",
    )      
print(result.final_output)