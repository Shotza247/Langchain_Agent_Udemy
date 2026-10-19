# main.py - loads config and runs the application
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from module.base import get_llm

load_dotenv()

llm = get_llm()

prompt_template = PromptTemplate.from_template(
    "What would a good company name be for a {name} company that sells {product}?"
)

# Format template with variables
selected_product_prompt = prompt_template.format(name="Investment", product="Trading Charts")
response = llm.invoke(selected_product_prompt)
print(response.content)
