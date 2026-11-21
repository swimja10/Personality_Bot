import anthropic
import gradio as gr

from main import run_turn

client = anthropic.Anthropic()
messages: list = []


def chat(message: str, history: list) -> str:
    start = len(messages)
    messages.append({"role": "user", "content": message})
    reply = run_turn(client, messages, verbose=False)
    if reply is None:
        del messages[start:]
        return "Something went wrong. Check the terminal for the error."
    return reply


demo = gr.ChatInterface(fn=chat, title="Kate")
demo.launch()
