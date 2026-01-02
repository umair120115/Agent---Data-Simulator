# def validate_object(obj: dict, schema: dict):
#     for k, spec in schema.items():
#         if k not in obj:
#             raise ValueError(f"Missing {k}")
#         t = spec["type"]
#         v = obj[k]
#         if t == "string" and not isinstance(v, str):
#             raise TypeError(k)
#         if t == "integer" and not isinstance(v, int):
#             raise TypeError(k)
#         if t == "decimal" and not isinstance(v, (int, float)):
#             raise TypeError(k)
def validate_object(obj: dict, schema: dict):
    for key in schema["required"]:
        if key not in obj:
            raise ValueError(f"Missing field: {key}")
