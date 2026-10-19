from dotenv import load_dotenv
load_dotenv()  # Automatically loads OPENAI_API_KEY from .env

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-5.1",temperature=0.9, max_completion_tokens=100)
prompt = 'What would a good company name be for a company that sells investments and trading charts?'

response = llm.invoke(prompt)
print(response.content)