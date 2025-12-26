from langgraph.graph import StateGraph, END

from app.nodes.intent_analyzer import analyze_intent
from app.nodes.load_schema import load_schema
from app.nodes.load_schema_definition import load_schema_definition
from app.nodes.build_execution_schema import build_execution_schema
from app.nodes.batch_planner import plan_batches
from app.nodes.generator import generate_batches
from app.nodes.enforce_schema import enforce_schema
from app.nodes.write_output import write_output

graph = StateGraph(dict)

graph.add_node("intent", analyze_intent)
graph.add_node("load_schema", load_schema)
graph.add_node("load_definition", load_schema_definition)
graph.add_node("build_execution_schema", build_execution_schema)
graph.add_node("batch_planner", plan_batches)
graph.add_node("generator", generate_batches)
graph.add_node("enforcer", enforce_schema)
graph.add_node("writer", write_output)

graph.set_entry_point("intent")
graph.add_edge("intent", "load_schema")
graph.add_edge("load_schema", "load_definition")
graph.add_edge("load_definition", "build_execution_schema")
graph.add_edge("build_execution_schema", "batch_planner")
graph.add_edge("batch_planner", "generator")
graph.add_edge("generator", "enforcer")
graph.add_edge("enforcer", "writer")
graph.add_edge("writer", END)

app = graph.compile()
