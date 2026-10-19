# main.py - loads config and runs the application
from dotenv import load_dotenv
load_dotenv()

from module.base import get_llm

llm = get_llm()
prompt = "What would a good company name be for a trading company?"
response = llm.invoke(prompt)
print(response.content)