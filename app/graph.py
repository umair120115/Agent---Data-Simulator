# # from langgraph.graph import StateGraph, END
# # from app.nodes.generator import generate_json
# # from app.nodes.validator import validate_output

# # class AgentState(dict):
# #     instruction: str
# #     output: dict
# #     status: str

# # graph = StateGraph(AgentState)

# # graph.add_node("generator", generate_json)
# # graph.add_node("validator", validate_output)

# # graph.set_entry_point("generator")

# # graph.add_edge("generator", "validator")

# # def route(state):
# #     if state["status"] == "valid":
# #         return END
# #     return "generator"

# # graph.add_conditional_edges("validator", route)

# # app = graph.compile()




# from typing import List
# from app.schemas import DatasetSchema
# from langgraph.graph import StateGraph, END,Send
# class AgentState(dict):
#     requirement: str
#     num_columns: int
#     num_rows: int
#     schema: DatasetSchema
#     batches: List[dict]
#     batch_results: List[list]
#     final_data: list

# def fan_out_batches(state: dict):
#     return [
#         Send(
#             "generator",
#             {
#                 "schema": state["schema"],
#                 "batch": batch
#             }
#         )
#         for batch in state["batches"]
#     ]


# def generate_batches(state: dict):
#     all_rows = []

#     for batch in state["batches"]:
#         rows = generate_single_batch(
#             schema=state["schema"],
#             batch=batch
#         )
#         all_rows.extend(rows)

#     return {"final_data": all_rows}

# # from langgraph.graph import StateGraph, END
# from langgraph.graph import StateGraph, END
# from app.nodes.schema_generator import generate_schema
# from app.nodes.batch_planner import plan_batches
# from app.nodes.generator import generate_batch
# from app.nodes.aggregator import aggregate_batches

# # graph = StateGraph(AgentState)

# # graph.add_node("schema", generate_schema)
# # graph.add_node("planner", plan_batches)
# # graph.add_node("generator", generate_batch)
# # graph.add_node("aggregator", aggregate_batches)

# # graph.set_entry_point("schema")
# # # graph.add_edge("schema", "planner")
# # graph.add_conditional_edges("planner", fan_out_batches)
# # graph.add_edge("planner", "generator")
# # graph.add_edge("generator", "aggregator")
# # graph.add_edge("aggregator", END)

# # app = graph.compile()

# graph = StateGraph(AgentState)

# graph.add_node("schema", generate_schema)
# graph.add_node("planner", plan_batches)
# graph.add_node("fanout", fan_out_batches)
# graph.add_node("generator", generate_batch)
# graph.add_node("aggregator", aggregate_batches)

# graph.set_entry_point("schema")

# graph.add_edge("schema", "planner")
# graph.add_edge("planner", "fanout")

# # Fan-out to generator
# graph.add_edge("fanout", "generator")

# # Collect all generator outputs
# graph.add_edge("generator", "aggregator")
# graph.add_edge("aggregator", END)

# app = graph.compile()




from langgraph.graph import StateGraph, END
from typing import List

from app.nodes.schema_generator import generate_schema
from app.nodes.batch_planner import plan_batches
from app.nodes.generator import generate_batches
from app.schemas import DatasetSchema


# ---------------------------
# Graph State Definition
# ---------------------------

class AgentState(dict):
    requirement: str
    num_columns: int
    num_rows: int
    schema: DatasetSchema
    batches: List[dict]
    final_data: List[dict]


# ---------------------------
# Graph Construction
# ---------------------------

graph = StateGraph(AgentState)

# Nodes
graph.add_node("schema", generate_schema)
graph.add_node("planner", plan_batches)
graph.add_node("generator", generate_batches)

# Flow
graph.set_entry_point("schema")
graph.add_edge("schema", "planner")
graph.add_edge("planner", "generator")
graph.add_edge("generator", END)

# Compile
app = graph.compile()
