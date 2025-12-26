# #for knowing the intent of the user  this node will interpret the intent of the user
# from app.llm import get_llm

# import json
# from langchain_core.prompts import ChatPromptTemplate
# from app.llm import get_llm


# def analyze_intent(state: dict):
#     if "prompt" not in state:
#         raise ValueError("Prompt missing")

#     llm = get_llm()

#     prompt = ChatPromptTemplate.from_messages([
#         ("system",
#          "You are an intent analysis agent.\n"
#          "Your task is to analyze a user request and extract:\n"
#          "- domain\n"
#          "- task_type\n"
#          "- data_sensitivity\n"
#          "- recommended_tools\n\n"
#          "Respond ONLY in valid JSON."),
#         ("human",
#          "{user_prompt}")
#     ])

#     response = llm.invoke(
#         prompt.format(user_prompt=state["prompt"])
#     )

#     try:
#         intent = json.loads(response.content)
#     except Exception:
#         raise RuntimeError(f"Invalid intent JSON: {response.content}")

#     return {
#         **state,
#         "domain": intent.get("domain"),
#         "task_type": intent.get("task_type"),
#         "data_sensitivity": intent.get("data_sensitivity"),
#         "recommended_tools": intent.get("recommended_tools", [])
#     }

import json
import re
from langchain_core.prompts import ChatPromptTemplate
from app.llm import get_llm


def extract_json(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?", "", text, flags=re.IGNORECASE).strip()
    text = re.sub(r"```$", "", text).strip()

    match = re.search(r"(\{.*\}|\[.*\])", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found")

    return match.group(1)


def analyze_intent(state: dict):
    if "prompt" not in state:
        raise ValueError("Prompt missing")

    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are an intent analysis agent.\n"
         "Analyze the user request and extract:\n"
         "- domain\n"
         "- task_type\n"
         "- data_sensitivity\n"
         "- recommended_tools\n\n"
         "Respond ONLY in valid JSON."),
        ("human", "{user_prompt}")
    ])

    chain = prompt | llm
    response = chain.invoke({"user_prompt": state["prompt"]})

    try:
        cleaned = extract_json(response.content)
        intent = json.loads(cleaned)
    except Exception as e:
        raise RuntimeError(
            f"Invalid intent JSON.\n"
            f"Raw output:\n{response.content}\n\n"
            f"Parsing error: {e}"
        )

    return {
        **state,
        "domain": intent.get("domain", "").lower(),
        "task_type": intent.get("task_type"),
        "data_sensitivity": intent.get("data_sensitivity"),
        "recommended_tools": intent.get("recommended_tools", [])
    }

