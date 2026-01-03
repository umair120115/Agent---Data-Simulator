# # app/nodes/planner.py
# import json
# from app.llm import get_llm
# from app.tools import tool_registry

# def planner(state):
#     llm = get_llm()
#     logger = tool_registry.get("reasoning_logger")

#     prompt = f"""
# User request:
# {state['prompt']}

# Decide rows and outputs.
# Return JSON:
# {{ "rows": number, "outputs": [{{"format":"json|csv|txt","path":"file"}}] }}
# """
#     raw = llm.invoke(prompt)
#     plan = json.loads(raw.content)

#     logger.log(f"Planner: {plan}")
#     return {**state, "plan": plan}



import json
from app.llm import get_llm
from app.tools import tool_registry
from app.utils.json_utils import extract_json

MAX_PLANNER_RETRIES = 3

def planner(state: dict):
    logger = tool_registry.get("reasoning_logger")
    llm = get_llm()

    logger.log("Planner: started reasoning")

    prompt = f"""
You are a planning agent.

User request:
{state['prompt']}

Decide:
- number of rows
- output files

STRICT RULES:
- Output ONLY valid JSON
- No explanations
- No markdown

Return EXACTLY:
{{
  "rows": number,
  "outputs": [
    {{ "format": "json|csv|txt", "path": "filename" }}
  ]
}}
"""

    last_error = None

    for attempt in range(MAX_PLANNER_RETRIES):
        logger.log(f"Planner attempt {attempt + 1}")

        raw = llm.invoke(prompt)
        raw_text = raw.content if hasattr(raw, "content") else str(raw)

        try:
            cleaned = extract_json(raw_text)
            plan = json.loads(cleaned)

            # Basic sanity checks
            if "rows" not in plan or "outputs" not in plan:
                raise ValueError("Planner JSON missing required keys")

            logger.log(f"Planner success: {plan}")
            return {**state, "plan": plan}

        except Exception as e:
            last_error = e
            logger.log(f"Planner failed: {e}")

    raise RuntimeError(
        f"Planner failed after {MAX_PLANNER_RETRIES} attempts.\n"
        f"Last error: {last_error}"
    )
