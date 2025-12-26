def plan_batches(state: dict):
    rows = state["rows"]
    batch_size = 25

    batches = []
    for i in range(0, rows, batch_size):
        batches.append({
            "batch_id": len(batches),
            "size": min(batch_size, rows - i)
        })

    return {
        **state,
        "batches": batches
    }
