import json, time, re
from app.llm import get_llm

def extract_array(text: str):
    text = re.sub(r"```(json)?", "", str(text), flags=re.I)
    match = re.search(r"\[.*\]", text, re.S)
    if not match:
        raise ValueError("No JSON array")
    return json.loads(match.group(0))

def generate_batches(state: dict):
    llm = get_llm()
    generated = []

    for batch in state["batches"]:
        for _ in range(3):
            messages = [
                {
                    "role": "system",
                    "content": (
                        "Generate synthetic data.\n"
                        "STRICT RULES:\n"
                        "- Output JSON array ONLY\n"
                        "- Follow schema EXACTLY\n"
                        "- No extra fields\n"
                        "- Ensure realistic diversity"
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Schema:\n{json.dumps(state['execution_schema'], indent=2)}\n\n"
                        f"Generate {batch['size']} records."
                    )
                }
            ]

            raw = llm.invoke(messages)
            raw_text = raw.content if hasattr(raw, "content") else raw

            try:
                generated.extend(extract_array(raw_text))
                break
            except Exception:
                time.sleep(1)

    return {**state, "generated_rows": generated}
