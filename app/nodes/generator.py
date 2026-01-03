# # app/nodes/generator.py
# import json
# from app.llm import get_llm

# def generate(state):
#     llm = get_llm()
#     rows = state["plan"]["rows"]
#     feedback = state.get("critic_feedback", "")

#     raw = llm.invoke(
#         f"Generate {rows} rows.\nSchema:{state['execution_schema']}\nFeedback:{feedback}"
#     )
#     data = json.loads(raw.content)

#     return {**state, "generated_rows": data}
import json
import time
from app.llm import get_llm
from app.tools import tool_registry
from app.utils.json_utils import extract_json

MAX_GEN_RETRIES = 3

def generate(state: dict):
    logger = tool_registry.get("reasoning_logger")
    llm = get_llm()

    execution_schema = state.get("execution_schema")
    rows = state.get("rows", 10)

    if not execution_schema:
        raise RuntimeError("Generator: execution_schema missing")

    prompt = f"""
You are a data generation agent.

STRICT RULES:
- Output ONLY valid JSON
- No explanations
- No markdown
- No code fences

Generate {rows} records strictly following this schema:

{json.dumps(execution_schema, indent=2)}
"""

    last_error = None

    for attempt in range(MAX_GEN_RETRIES):
        logger.log(f"Generator attempt {attempt + 1}")

        raw = llm.invoke(prompt)
        raw_text = raw.content if hasattr(raw, "content") else str(raw)

        try:
            cleaned = extract_json(raw_text)
            data = json.loads(cleaned)

            if not isinstance(data, list):
                raise ValueError("Generated data must be a JSON array")

            logger.log(f"Generator success: {len(data)} rows generated")

            return {
                **state,
                "generated_rows": data
            }

        except Exception as e:
            last_error = e
            logger.log(f"Generator failed: {e}")
            time.sleep(1)

    raise RuntimeError(
        f"Generator failed after {MAX_GEN_RETRIES} attempts.\n"
        f"Last error: {last_error}"
    )
