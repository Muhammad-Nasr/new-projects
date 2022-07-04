import os
from dotenv import load_dotenv
from yaml import load
import openai

load_dotenv()

openai.api_key = os.environ.get('OPEN_AI_KEY')

completion = openai.Completion()

start_chat_log = """Human: Hello, who are you?
AI: I am doing great. How can I help you today?
"""


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log

    prompt = f"{chat_log}Human: {question}\nAI:"
    response = completion.create(
        prompt=prompt,
        model='davinci', stop=['\nHuman'], temperature=.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
  
    return answer

# append more examples to chat log
def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f"{chat_log}Human: {question}\nAI: {answer}\n"
