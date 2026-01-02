import json
from app.llm import get_llm
from app.tools import tool_registry
from app.nodes.intent_analyzer import extract_json

def infer_schema_from_file(state: dict):
    if "input_file" not in state:
        raise ValueError(
            "input_file missing. Provide a file containing schema/sample data."
        )

    fs = tool_registry.get("filesystem")
    llm = get_llm()

    # Read PDF or text file (assumed already extracted to text)
    # raw_text = fs.read_text(state["input_file"])
    raw_text = state["input_text"]
# raw_text = raw_text[:6000]  # safety

    raw_text = raw_text[:6000]  # safety for LLM

    messages = [
        {
            "role": "system",
            "content": (
                "You are a schema inference agent.\n"
                "The user has provided a file containing sample data and/or a data dictionary.\n\n"
                "Your tasks:\n"
                "1. Infer the JSON schema (structure only)\n"
                "2. Infer schema_definition (field meanings)\n\n"
                "STRICT RULES:\n"
                "- Output ONLY valid JSON\n"
                "- No explanations\n"
                "- No markdown\n\n"
                "Return EXACTLY:\n"
                "{\n"
                '  "schema": { ... },\n'
                '  "schema_definition": { ... }\n'
                "}"
            )
        },
        {
            "role": "user",
            "content": raw_text
        }
    ]

    raw = llm.invoke(messages)
    raw_text = raw.content if hasattr(raw, "content") else raw

    inferred = json.loads(extract_json(raw_text))

    return {
        **state,
        "schema": inferred["schema"],
        "schema_definition": inferred["schema_definition"]
    }
