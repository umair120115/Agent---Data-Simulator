# from app.graph import app

# result = app.invoke({
#     "instruction": "Generate a realistic Indian user profile"
# })

# print(result["output"].model_dump())


# from app.graph import app

# result = app.invoke({
#     "requirement": "Banking transaction dataset",
#     "num_columns": 30,
#     "num_rows": 1000
# })

# print(len(result["final_data"]))


# import json
# from app.graph import app

# result = app.invoke({
#     "requirement": "Banking transaction dataset",
#     "num_columns": 15,
#     "num_rows": 100
# })

# data = result["final_data"]

# output_file = "output.txt"

# with open(output_file, "w", encoding="utf-8") as f:
#     for row in data:
#         f.write(json.dumps(row))
#         f.write("\n")

# print(f"Saved {len(data)} rows to {output_file}")
import json
from app.graph import app 

# 1. Run the agent
print("Invoking agent...")
result = app.invoke({
    "requirement": "Banking transaction dataset",
    "num_columns": 15,
    "num_rows": 100
})

# 2. Define debug file name
debug_filename = "debug_raw_response.txt"

# 3. Write the RAW result to file
with open(debug_filename, "w", encoding="utf-8") as f:
    f.write("--- RAW OUTPUT START ---\n")
    
    # Try to save as pretty JSON first (easier to read)
    try:
        f.write(json.dumps(result, indent=4, default=str))
    except Exception:
        # If JSON fails (e.g. complex objects), just force it to a string
        f.write(str(result))
        
    f.write("\n--- RAW OUTPUT END ---\n")

print(f"full response saved to '{debug_filename}'")