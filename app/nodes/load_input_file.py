import os
from app.tools import tool_registry

def load_input_file(state: dict):
    if "input_file" not in state:
        raise ValueError("input_file missing from state")

    path = state["input_file"]
    ext = os.path.splitext(path)[1].lower()

    if ext == ".pdf":
        reader = tool_registry.get("pdf_reader")
        text = reader.extract_text(path)

    else:
        fs = tool_registry.get("filesystem")
        text = fs.read_text(path)

    if not text.strip():
        raise RuntimeError("No text could be extracted from input file")

    return {
        **state,
        "input_text": text
    }
