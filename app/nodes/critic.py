# # app/nodes/critic.py
# import json
# from app.llm import get_llm

# def critic(state):
#     llm = get_llm()
#     sample = state["generated_rows"][:5]

#     raw = llm.invoke(
#         f"Critique data vs schema.\nSchema:{state['execution_schema']}\nData:{sample}"
#     )
#     result = json.loads(raw.content)

#     if result["decision"] == "retry":
#         return {**state, "retry": True, "critic_feedback": result["correction"]}
#     return {**state, "retry": False}
import json
import time
from app.llm import get_llm
from app.tools import tool_registry
from app.utils.json_utils import extract_json

MAX_CRITIC_RETRIES = 3

def critic(state: dict):
    logger = tool_registry.get("reasoning_logger")
    llm = get_llm()

    generated = state.get("generated_rows", [])
    execution_schema = state.get("execution_schema")

    if not generated or not execution_schema:
        raise RuntimeError("Critic: missing generated data or schema")

    prompt = f"""
You are a data quality critic agent.

Evaluate whether the following generated data strictly conforms
to the given schema.

Return ONLY valid JSON:
{{
  "accepted": true | false,
  "issues": ["..."]
}}

Schema:
{json.dumps(execution_schema, indent=2)}

Generated data sample:
{json.dumps(generated[:3], indent=2)}
"""

    last_error = None

    for attempt in range(MAX_CRITIC_RETRIES):
        logger.log(f"Critic attempt {attempt + 1}")

        raw = llm.invoke(prompt)
        raw_text = raw.content if hasattr(raw, "content") else str(raw)

        try:
            cleaned = extract_json(raw_text)
            result = json.loads(cleaned)

            if not isinstance(result, dict) or "accepted" not in result:
                raise ValueError("Invalid critic response structure")

            logger.log(f"Critic decision: {result['accepted']}")

            return {
                **state,
                "critic_result": result
            }

        except Exception as e:
            last_error = e
            logger.log(f"Critic failed: {e}")
            time.sleep(1)

    raise RuntimeError(
        f"Critic failed after {MAX_CRITIC_RETRIES} attempts.\n"
        f"Last error: {last_error}"
    )
