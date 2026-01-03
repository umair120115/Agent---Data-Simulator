# # app/nodes/tool_planner.py
# import json
# from app.llm import get_llm
# from app.tools import tool_registry

# def tool_planner(state):
#     llm = get_llm()
#     tools = list(tool_registry._tools.keys())

#     raw = llm.invoke(f"Select tools for task.\nTools:{tools}\nTask:{state['plan']}")
#     tool_plan = json.loads(raw.content)

#     return {**state, "tool_plan": tool_plan}
import json
from app.llm import get_llm
from app.tools import tool_registry
from app.utils.json_utils import extract_json

MAX_TOOL_PLANNER_RETRIES = 3

def tool_planner(state: dict):
    logger = tool_registry.get("reasoning_logger")
    llm = get_llm()

    available_tools = list(tool_registry._tools.keys())

    logger.log("Tool planner: started reasoning")

    prompt = f"""
You are a tool selection agent.

Task plan:
{state.get("plan")}

Available tools:
{available_tools}

STRICT RULES:
- Output ONLY valid JSON
- No explanations
- No markdown

Return a JSON array of tool names, for example:
["filesystem", "pdf_reader", "csv_writer"]
"""

    last_error = None

    for attempt in range(MAX_TOOL_PLANNER_RETRIES):
        logger.log(f"Tool planner attempt {attempt + 1}")

        raw = llm.invoke(prompt)
        raw_text = raw.content if hasattr(raw, "content") else str(raw)

        try:
            cleaned = extract_json(raw_text)
            tool_plan = json.loads(cleaned)

            if not isinstance(tool_plan, list):
                raise ValueError("Tool plan must be a list")

            logger.log(f"Tool planner success: {tool_plan}")
            return {**state, "tool_plan": tool_plan}

        except Exception as e:
            last_error = e
            logger.log(f"Tool planner failed: {e}")

    raise RuntimeError(
        f"Tool planner failed after {MAX_TOOL_PLANNER_RETRIES} attempts.\n"
        f"Last error: {last_error}"
    )
