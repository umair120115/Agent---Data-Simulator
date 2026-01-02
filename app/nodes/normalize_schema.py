# import json
# from app.llm import get_llm
# from app.tools import tool_registry
# from app.nodes.intent_analyzer import extract_json

# def infer_schema_from_file(state: dict):
#     fs = tool_registry.get("filesystem")
#     llm = get_llm()

#     raw_text = fs.read_text(state["schema_path"])
#     raw_text = raw_text[:6000]  # safety

#     messages = [
#         {
#             "role": "system",
#             "content": (
#                 "Infer JSON schema and schema_definition from sample data.\n"
#                 "Return ONLY JSON:\n"
#                 "{ \"schema\": {...}, \"schema_definition\": {...} }"
#             )
#         },
#         {"role": "user", "content": raw_text}
#     ]

#     raw = llm.invoke(messages)
#     raw_text = raw.content if hasattr(raw, "content") else raw
#     inferred = json.loads(extract_json(raw_text))

#     return {
#         **state,
#         "schema": inferred["schema"],
#         "schema_definition": inferred["schema_definition"]
#     }
def normalize_schema(state: dict):
    schema = state["schema"]

    # ensure object schema
    if "type" not in schema:
        schema = {
            "type": "object",
            "properties": schema,
            "required": list(schema.keys())
        }

    return {**state, "normalized_schema": schema}
