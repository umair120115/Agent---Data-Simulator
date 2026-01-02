def build_execution_schema(state: dict):
    return {
        **state,
        "execution_schema": state["normalized_schema"]
    }
