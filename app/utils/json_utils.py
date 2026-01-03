import re

def extract_json(text: str) -> str:
    if not text or not isinstance(text, str):
        raise ValueError("Empty or invalid LLM response")

    # Remove markdown fences
    text = re.sub(r"```(json)?", "", text, flags=re.IGNORECASE).strip()

    # Find first JSON object or array
    match = re.search(r"(\{.*\}|\[.*\])", text, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON found in:\n{text}")

    return match.group(1)
