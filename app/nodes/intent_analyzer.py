import json, re
from app.llm import get_llm

def extract_json(text: str) -> str:
    text = re.sub(r"```(json)?", "", str(text), flags=re.I).strip()
    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        raise ValueError("No JSON found")
    return match.group(0)

def analyze_intent(state: dict):
    llm = get_llm()

    messages = [
        {
            "role": "system",
            "content": (
                "You analyze user intent.\n"
                "Return ONLY JSON with keys:\n"
                "domain, task_type, data_sensitivity, recommended_tools"
            )
        },
        {"role": "user", "content": state["prompt"]}
    ]

    raw = llm.invoke(messages)
    raw_text = raw.content if hasattr(raw, "content") else raw
    intent = json.loads(extract_json(raw_text))

    return {**state, **intent}
