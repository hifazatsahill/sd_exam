from agents import Agent,Runner,ModelSettings,function_tool
from openai.types import Reasoning
from agents import set_tracing_disabled,enable_verbose_stdout_logging
import os
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(disabled=True)

enable_verbose_stdout_logging()


# @function_tool
# def guardrail_prompt():
#     return f"You are specilized for pakistan studies and you have to answer all the questions related to pakistan studies only otherwise you have to say i am sorry i can only answer the questions related to pakistan studies."

start_agent=Agent(
    name="Assitant",
    instructions="You are responsible user query.",
    # agr ham apny agent ko instruction ma kisi tool ka ya agent ka use krna restirict karain to wo unhain use nae kareega
    model="gpt-4o",
    model_settings=ModelSettings(
        # frequency_penalty=0.01,(ya bar bar anay waly words ko rokta ha uniqe words provide krta ha )
        # reasoning=Reasoning(
        # #     effect="auto"
        #     generate_summary='concise',
        #     # ya ya extra text ko cut krta ha aur short ma clear answer krta ha conclosion dataa ha

        # ),

        # presence_penalty=1.0,
        # truncation="auto",
        # ya ya extra text ko cut krta ha aur short ma clear answer krta ha
        # presence_penalty=0.01,(ya bar bar anay waly words ko rokta ha uniqe words provide krta ha )
        # max_token=25,
        metadata={"project": "agents"},
                # YA Tracing aur debuging ka liya use hota  ha aor iski type str he pass krsaktay hain
                # trace_id="my_trace_id",(key and value pass krna hoga)
        store=True  # ya ya apky data ko store krta ha

        ),
        # temperature=0.1,(Ya user ki Query ko check krta ha aur according to temperature value answer provide krta ha)

    # tools=[guardrail_prompt],
)

result = Runner.run_sync(
    start_agent,
    "Hello",
)
print(result.final_output)



