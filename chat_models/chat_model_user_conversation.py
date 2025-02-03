from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage,SystemMessage



load_dotenv()


llm = ChatOpenAI(model="gpt-4o")


# creating an array to save chat with llm
chat_history = []


system_message = SystemMessage(content="Your role is to become a good career counseler")

# appending/adding system message to chat-history array at start
chat_history.append(system_message)


# chat loop - it will ask to take input from you until you didn't type exit and give to ai to respond
while True:
    query = input("you :")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))
    
    
    # now invoking llm with human message and print
    response = llm.invoke(chat_history)
    result = response.content
    chat_history.append(AIMessage(content=result))
    
    print(f"AI Response: ${result}")
    
    

print("-------Message History-------")
print(chat_history)
