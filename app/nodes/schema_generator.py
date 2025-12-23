from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from app.llm import get_llm
from app.schemas import DatasetSchema

parser = PydanticOutputParser(pydantic_object=DatasetSchema)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a senior data architect. Design realistic dataset schemas."),
    ("human",
     "Requirement: {requirement}\n"
     "Number of columns: {num_columns}\n"
     "{format_instructions}")
])

def generate_schema(state: dict):
    llm = get_llm()
    chain = prompt | llm | parser

    schema = chain.invoke({
        "requirement": state["requirement"],
        "num_columns": state["num_columns"],
        "format_instructions": parser.get_format_instructions()
    })

    return {"schema": schema}
