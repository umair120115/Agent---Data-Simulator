# import json
# from app.tools import tool_registry

# def write_output(state: dict):
#     fs = tool_registry.get("filesystem")
#     output = state["output"]

#     fs.write_text(
#         output["path"],
#         json.dumps(state["final_data"], indent=2)
#     )

#     return state
from app.tools import tool_registry

def write_output(state: dict):
    output_cfg = state.get("output")

    if not output_cfg:
        return state  # optional output

    path = output_cfg.get("path", "output.json")
    fmt = output_cfg.get("format", "json")

    writer = tool_registry.get("json_writer")

    # Prefer validated data, fallback to generated
    data = state.get("final_data") or state.get("generated_rows")

    if not data:
        raise RuntimeError("No data available to write")

    if fmt == "json":
        writer.write(path, data)
    elif fmt == "txt":
        # still write JSON, but as text
        writer.write(path, data)
    else:
        raise ValueError(f"Unsupported output format: {fmt}")

    return {
        **state,
        "output_written": path
    }
