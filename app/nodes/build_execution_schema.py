def build_execution_schema(state: dict):
    schema = state["schema"]
    definition = state["schema_definition"]

    execution = {}

    for section, fields in schema.items():
        if isinstance(fields, list):
            execution[section] = {
                "type": "array",
                "items": {
                    k: {
                        "type": v,
                        "description": definition.get(k, {}).get("description", "")
                    }
                    for k, v in fields[0].items()
                }
            }
        else:
            execution[section] = {
                k: {
                    "type": v,
                    "description": definition.get(k, {}).get("description", "")
                }
                for k, v in fields.items()
            }

    return {**state, "execution_schema": execution}
