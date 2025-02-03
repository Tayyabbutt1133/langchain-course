from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# here we are loading private key's from .env file, it will automatically load all available keys working under the hood for us
load_dotenv()

# We are initializing openai-llm model, also we can use any other model as well.
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Simply passing question to ai model to respond
question = "What is Generative AI ?"
response = llm.invoke(question)

# printing response from LLM Model
print("Full AI Result :")
print(response)
print("Only Content :")
print(response.content) # it will print only main response/content
print("Only Metadata :")
print(response.response_metadata) # only metadata include tokens consume to perform task
