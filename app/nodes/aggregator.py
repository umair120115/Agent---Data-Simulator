# Keeps memory organized

# Enables streaming / persistence later

# def aggregate_batches(state: dict):
#     final_rows = []

#     for batch in state["batch_results"]:
#         final_rows.extend(batch)

#     return {"final_data": final_rows}


def aggregate_batches(state: dict):
    final_rows = []

    for result in state["generator"]:
        final_rows.extend(result["rows"])

    return {"final_data": final_rows}
