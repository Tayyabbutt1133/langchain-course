from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

# now using different model of OpenAI
openai_llm = ChatOpenAI(model="gpt-4o")
# claude_llm = ChatAnthropic(model="claude-3-5-haiku-20241022",temperature=0,
#     max_tokens=1024,
#     timeout=None)
gemini_llm = GoogleGenerativeAI(model="gemini-1.5-flash")




# What is System Message ? 
# System message actually gives any Ai model, a sort of context in terms of purpose of using while doing conversations, it is best practice to do it at start for once


# Creating Chat conversation array to pass ai model instead of just string to make it more conversational
message = [
    SystemMessage(content="You are a Mathematician solving complex Problems"),
    HumanMessage(content="Find the perimeter of a triangle with sides 7 cm, 9 cm, and 12 cm.")
]


# response = llm.invoke(message)
# print(f"Response from AI : ${response.content}")


# now we are making a back-and-forth conversations with AI Model
messages = [
    SystemMessage(content="Solving complex maybe problems"),
    HumanMessage(content="What is 81 divided by 9 ?"),
    AIMessage(content="81 divided by 9 is 9"),
    HumanMessage(content="Sarah has 23 apples. She buys 15 more apples from the store. How many apples does she have now ?")
]



response = openai_llm.invoke(messages)
print("AI Response : ")
print(response)
