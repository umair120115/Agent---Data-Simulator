import json

def write_output(state: dict):
    path = state["output"]["path"]

    with open(path, "w", encoding="utf-8") as f:
        for row in state["final_data"]:
            f.write(json.dumps(row))
            f.write("\n")

    return state
