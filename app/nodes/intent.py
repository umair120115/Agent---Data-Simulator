# app/nodes/intent.py
from app.tools import tool_registry

def intent(state):
    tool_registry.get("reasoning_logger").log("Intent received")
    return state
