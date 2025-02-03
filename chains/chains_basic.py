from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI


load_dotenv()



llm = ChatOpenAI(model="gpt-4o")


prompt = ChatPromptTemplate.from_messages(
    [
    ("system", "You need to give Use-cases of Generative AI in {industry}"),
    ("human", "Usecases needs to be at least {count}"),
    ]
)


chain = prompt | llm | StrOutputParser()

result = chain.invoke({
    "industry" : "Healthcare",
    "count" : "5"
   })

print(result)
















