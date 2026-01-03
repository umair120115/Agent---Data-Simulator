# app/nodes/load_input.py
from app.tools import tool_registry

def load_input(state):
    fs = tool_registry.get("filesystem")
    pdf = tool_registry.get("pdf_reader")
    texts = []

    for f in state.get("input_files", []):
        texts.append(pdf.extract_text(f) if f.endswith(".pdf") else fs.read_text(f))

    return {**state, "input_text": "\n".join(texts)}
