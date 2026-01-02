def plan_batches(state: dict):
    rows = state["rows"]
    batch_size = 50

    batches = []
    while rows > 0:
        size = min(batch_size, rows)
        batches.append({"size": size})
        rows -= size

    return {**state, "batches": batches}
