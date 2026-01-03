# app/nodes/write_output.py
from app.tools import tool_registry

def write_output(state):
    for out in state["plan"]["outputs"]:
        writer = tool_registry.get(f"{out['format']}_writer")
        writer.write(out["path"], state["generated_rows"])
    return state
