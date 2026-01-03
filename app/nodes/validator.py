# app/nodes/validator.py
def validate(state):
    return {**state, "valid_rows": state["generated_rows"], "invalid_rows": []}
