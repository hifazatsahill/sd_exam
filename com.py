from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

response=client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Explain python in short",
    max_tokens=15,
    logprobs=5,
)

for choice in response.choices:
    for token,logprob in zip(choice.logprobs.tokens,choice.logprobs.token_logprobs):
        print(f"Token: {token}, LogProb: {logprob}")
