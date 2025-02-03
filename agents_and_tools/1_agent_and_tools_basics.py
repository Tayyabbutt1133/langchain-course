from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI



load_dotenv()


# defining tool calling definition
def get_current_time(*args, **kwargs):
    """Returns the current time in H:MM AM/PM format."""
    import datetime
    
    now = datetime.datetime.now() # get current time
    return now.strftime("%I:%M %p")




# defining list of tools available to agent
tools = [
    Tool(
        name="Time",
        func= get_current_time,
        description="It will get latest current time"
    )
]

prompt = hub.pull("hwchase17/react")


llm = ChatOpenAI(model="gpt-3.5-turbo")



agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
    stop_sequence=True
)


agent_executor = AgentExecutor.from_agent_and_tools(
      agent=agent,
      tools=tools,
      verbose= True         
)


response = agent_executor.invoke({"input": "What time is it ?"})



print(f"response : ${response}")





    
