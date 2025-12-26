from app.validators.schema_validator import validate_object

def enforce_schema(state: dict):
    valid = []
    invalid = []

    for row in state["generated_rows"]:
        try:
            validate_object(
                row["portfolio_summary"],
                state["execution_schema"]["portfolio_summary"]
            )
            for h in row["holdings"]:
                validate_object(
                    h,
                    state["execution_schema"]["holdings"]["items"]
                )
            valid.append(row)
        except Exception as e:
            invalid.append({"row": row, "error": str(e)})

    return {**state, "final_data": valid, "invalid_rows": invalid}
