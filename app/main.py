# import json
# from app.graph import app

# print("Invoking agent...")

# result = app.invoke({
#     "prompt": "Generate realistic investment portfolio data",
#     "rows": 50,
#     "input_file": "JSON_Sample.pdf",   # NEW (optional)
#     "output": {
#         "format": "txt",
#         "path": "output.txt"
#     }
# })

# with open("debug_raw_response.txt", "w", encoding="utf-8") as f:
#     f.write(json.dumps(result, indent=2, default=str))

# print("Agent execution completed successfully.")





# import json
# from app.graph import app

# print("Invoking autonomous agent...")

# result = app.invoke({
#     "prompt": (
#         "Generate 50 synthetic financet records "
#         "using the attached file for schema. "
#         "Export both JSON and CSV outputs."
#     ),
#     "input_files": ["JSON_Sample.pdf"]
# })

# # Debug full state
# with open("debug_raw_response.txt", "w", encoding="utf-8") as f:
#     f.write(json.dumps(result, indent=2, default=str))

# print("Agent execution completed.")

from app.graph import app

app.invoke({
    "prompt": "Generate 50 synthetic healthcare patient records and output JSON and CSV",
    "input_files": ["health_sample.txt"]
})

