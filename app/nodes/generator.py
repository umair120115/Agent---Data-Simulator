import json, time
from langchain_core.prompts import ChatPromptTemplate
from app.llm import get_llm

def safe_json(text):
    return json.loads(text.replace("```json", "").replace("```", "").strip())

def generate_batches(state: dict):
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are an autonomous synthetic data generation agent.\n"
         "The execution schema is authoritative.\n"
         "Generate realistic, diverse, schema-compliant JSON.\n"
         "Return ONLY valid JSON."),
        ("human",
         "User intent:\n{prompt}\n\n"
         "Execution schema:\n{schema}\n\n"
         "Generate {n} records.")
    ])

    generated = []

    for batch in state["batches"]:
        for _ in range(3):
            response = llm.invoke(prompt.format(
                prompt=state["prompt"],
                schema=json.dumps(state["execution_schema"], indent=2),
                n=batch["size"]
            ))
            try:
                generated.extend(safe_json(response.content))
                break
            except Exception:
                time.sleep(1)
        else:
            raise RuntimeError("LLM failed to produce valid JSON")

    return {**state, "generated_rows": generated}

