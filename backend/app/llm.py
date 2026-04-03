
import yaml
from openai import OpenAI
from app.memory import get_memory, save_memory
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("assistant.yaml") as f:
    config = yaml.safe_load(f)

def generate_reply(user_input):
    memories = get_memory(user_input)
    context = "\n".join(memories)

    messages = [
        {"role": "system", "content": config["assistant"]["system_prompt"] + context},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model=config["model"]["name"],
        messages=messages
    )

    reply = response.choices[0].message.content
    save_memory(user_input + " " + reply)

    return reply
