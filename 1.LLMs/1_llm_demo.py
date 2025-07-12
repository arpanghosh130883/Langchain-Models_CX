from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Get the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI LLM
llm = OpenAI(api_key=api_key, model='gpt-3.5-turbo-instruct')

#llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India")

print(result)
