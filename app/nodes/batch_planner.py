# We cannot say to p[rint 1000 at once so divided all into batches like 10*100]

def plan_batches(state: dict):
    total_rows = state["num_rows"]
    batch_size = 100

    batches = []
    for start in range(0, total_rows, batch_size):
        batches.append({
            "batch_id": len(batches),
            "size": min(batch_size, total_rows - start)
        })

    return {"batches": batches}
