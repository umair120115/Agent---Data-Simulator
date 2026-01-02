from app.validators.schema_validator import validate_object

def enforce_schema(state: dict):
    valid, invalid = [], []

    for row in state["generated_rows"]:
        try:
            validate_object(row, state["execution_schema"])
            valid.append(row)
        except Exception as e:
            invalid.append({"row": row, "error": str(e)})

    return {
        **state,
        "final_data": valid,
        "invalid_rows": invalid
    }
