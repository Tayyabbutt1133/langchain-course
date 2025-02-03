from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv


load_dotenv()

# Template string with chat prompt template or PromptTemplate 

# # Part 1 -> Creating a ChatPromptTemplate using simple string 
# template = "Tell me some jokes about {topic}"
# prompt_template = ChatPromptTemplate.from_template(template)
# print("----------Prompt from template-----------")
# response = prompt_template.invoke({"topic" : "lawyers"})
# print(response)

# Doc string

# # Part 2 -> creating chatpromptTemplate with multiple arguments 
# multi_template = """You are an helpful AI Assistant.
# Human: Tell me a {adjective} about {animals}.
# Assistant:"""
# prompt_multi_template = ChatPromptTemplate.from_template(multi_template)
# print("----------Prompt from template-----------")
# result = prompt_multi_template.invoke({
#     "adjective" : "Funny",
#     "animals" : "lions",
# })
# print(result)



# Part 3 ->Prompt with system and human messages using tuple 

messages = [
        ("system", "You are an AI Assistant telling jokes about {topic}."),
        ("human", "Tell {total_count} jokes.")
]
prompt = ChatPromptTemplate.from_messages(messages)
response = prompt.invoke({"topic": "lawyers", "total_count": 3})
print(response)



# # Extra Informoation about Part 3.
# # This does work:
# messages = [
#     ("system", "You are a comedian who tells jokes about {topic}."),
#     HumanMessage(content="Tell me 3 jokes."),
# ]
# prompt_template = ChatPromptTemplate.from_messages(messages)
# prompt = prompt_template.invoke({"topic": "lawyers"})
# print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
# print(prompt)


# This does NOT work:
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    HumanMessage(content="Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
print(prompt)