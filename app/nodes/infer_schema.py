# # app/nodes/infer_schema.py
# import json
# from app.llm import get_llm

# def infer_schema(state):
#     llm = get_llm()
#     raw = llm.invoke(f"Infer JSON schema from:\n{state['input_text'][:6000]}")
#     schema = json.loads(raw.content)
#     return {**state, "raw_schemas": [schema]}

import json
from app.llm import get_llm
from app.tools import tool_registry
from app.utils.json_utils import extract_json

MAX_SCHEMA_RETRIES = 3

def infer_schema(state: dict):
    logger = tool_registry.get("reasoning_logger")
    llm = get_llm()

    input_text = state.get("input_text", "")
    if not input_text.strip():
        raise RuntimeError("infer_schema: input_text is empty")

    logger.log("Schema inference: started")

    prompt = f"""
You are a schema inference agent.

Infer a JSON schema from the following content.

STRICT RULES:
- Output ONLY valid JSON
- No explanations
- No markdown
- No code fences

Return a single JSON object describing the schema.

Content:
{input_text[:6000]}
"""

    last_error = None

    for attempt in range(MAX_SCHEMA_RETRIES):
        logger.log(f"Schema inference attempt {attempt + 1}")

        raw = llm.invoke(prompt)
        raw_text = raw.content if hasattr(raw, "content") else str(raw)

        try:
            cleaned = extract_json(raw_text)
            schema = json.loads(cleaned)

            if not isinstance(schema, dict):
                raise ValueError("Schema must be a JSON object")

            logger.log("Schema inference: success")

            return {
                **state,
                "raw_schemas": state.get("raw_schemas", []) + [schema]
            }

        except Exception as e:
            last_error = e
            logger.log(f"Schema inference failed: {e}")

    raise RuntimeError(
        f"Schema inference failed after {MAX_SCHEMA_RETRIES} attempts.\n"
        f"Last error: {last_error}"
    )
