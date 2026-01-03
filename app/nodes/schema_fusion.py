# app/nodes/schema_fusion.py
def schema_fusion(state):
    merged = {}
    for s in state["raw_schemas"]:
        merged.update(s)
    return {**state, "merged_schema": merged}
