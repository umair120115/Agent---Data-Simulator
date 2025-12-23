# #Dynamic schema generator 

# import json
# from langchain_core.prompts import ChatPromptTemplate
# from app.llm import get_llm

# prompt = ChatPromptTemplate.from_messages([
#     ("system",
#      "You generate realistic synthetic data strictly following the schema."),
#     ("human",
#      "Schema:\n{schema}\n"
#      "Generate {batch_size} rows.\n"
#      "Return ONLY a JSON array.")
# ])

# def generate_batch(state: dict):
#     llm = get_llm()

#     response = llm.invoke(prompt.format(
#         schema=state["schema"].model_dump(),
#         batch_size=state["batch"]["size"]
#     ))

#     rows = json.loads(response.content)

#     return {"rows": rows}


import json
from langchain_core.prompts import ChatPromptTemplate
from app.llm import get_llm
import json
import re

def safe_json_load(text: str):
    if not text or not text.strip():
        raise ValueError("Empty response from LLM")

    # Remove markdown code fences if present
    text = text.strip()
    text = re.sub(r"^```json", "", text)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)

    return json.loads(text)
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You generate realistic synthetic data strictly following the schema."),
    ("human",
     "Schema:\n{schema}\n"
     "Generate {batch_size} rows.\n"
     "Return ONLY a JSON array.")
])


from langchain_core.prompts import ChatPromptTemplate
from app.llm import get_llm
import time

def generate_batches(state: dict):
    llm = get_llm()
    all_rows = []

    for batch in state["batches"]:
        retries = 3

        for attempt in range(retries):
            response = llm.invoke(
                prompt.format(
                    schema=state["schema"].model_dump(),
                    batch_size=batch["size"]
                )
            )

            try:
                rows = safe_json_load(response.content)
                all_rows.extend(rows)
                print(f"Generated batch {batch['batch_id']}")
                break

            except Exception as e:
                print(
                    f"Batch {batch['batch_id']} failed "
                    f"(attempt {attempt + 1}/{retries}): {e}"
                )
                time.sleep(1)

        else:
            raise RuntimeError(
                f"Failed to generate valid JSON for batch {batch['batch_id']}"
            )

    return {"final_data": all_rows}
