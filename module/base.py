# base.py - defines models, prompts, or helper chains
from langchain_openai import ChatOpenAI

def get_llm():
    return ChatOpenAI(model="gpt-5.1", temperature=0.9,max_completion_tokens=100)