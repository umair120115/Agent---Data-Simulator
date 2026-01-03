# app/nodes/build_execution_schema.py
def build_execution_schema(state):
    return {**state, "execution_schema": state["merged_schema"]}
