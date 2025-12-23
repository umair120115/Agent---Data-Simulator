def validate_output(state: dict):
    if state.get("output"):
        return {"status": "valid"}
    return {"status": "invalid"}
