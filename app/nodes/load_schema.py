from app.tools import tool_registry

def load_schema(state: dict):
    fs = tool_registry.get("filesystem")
    schema = fs.load_json(state["schema_path"])

    return {
        **state,
        "schema": schema
    }
