def normalize_schema(state: dict):
    schema = state["schema"]
    definition = state["schema_definition"]

    return {
        **state,
        "execution_schema": {
            "schema": schema,
            "definition": definition
        }
    }
# To normalize the schema according to the definition provided