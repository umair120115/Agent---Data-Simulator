import json
from app.graph import app

print("Invoking agent...")

result = app.invoke({
    "prompt": "Generate realistic banking investment portfolio data",
    "rows": 100,
    "schema_path": "schema.json",
    "schema_definition_path": "schema_definition.xlsx",
    "output": {
        "format": "txt",
        "path": "output.txt"
    }
})

with open("debug_raw_response.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(result, indent=2, default=str))

print("Agent execution completed successfully.")
