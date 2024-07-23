import anthropic
from helpers.anthropic_helpers.tools.navigate import navigate
from dotenv import load_dotenv
import os

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_KEY"))

tools_arr = [navigate]

def chat_with_claude(messages_arr):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=2000,
        temperature=0,
        system="If a tool was used to process the request, please say so at the beginning of your response. If you don't have a tool to answer the question, answer it using your existing knowledge.",
        messages=messages_arr,
        tool_choice={"type": "auto"},
        tools=tools_arr
    )
    return message
