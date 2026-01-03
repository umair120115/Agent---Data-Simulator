
# from langgraph.graph import StateGraph, END

# # ===== Nodes =====
# from app.nodes.intent_analyzer import analyze_intent
# from app.nodes.load_input_file import load_input_file
# from app.nodes.infer_schema_from_file import infer_schema_from_file
# from app.nodes.normalize_schema import normalize_schema
# from app.nodes.build_execution_schema import build_execution_schema
# from app.nodes.plan_batches import plan_batches
# from app.nodes.generator import generate_batches
# from app.nodes.enforce_schema import enforce_schema
# from app.nodes.write_output import write_output


# # ===== Graph Definition =====
# graph = StateGraph(dict)

# # ----- Register Nodes -----
# graph.add_node("intent", analyze_intent)
# graph.add_node("load_input", load_input_file)
# graph.add_node("infer_schema", infer_schema_from_file)
# graph.add_node("normalize_schema", normalize_schema)
# graph.add_node("build_execution_schema", build_execution_schema)
# graph.add_node("plan_batches", plan_batches)
# graph.add_node("generate", generate_batches)
# graph.add_node("validate", enforce_schema)
# graph.add_node("write", write_output)

# # ----- Entry Point -----
# graph.set_entry_point("intent")

# # ----- Execution Flow -----
# graph.add_edge("intent", "load_input")                 # decide + load schema source
# graph.add_edge("load_input", "infer_schema")           # infer schema + definition
# graph.add_edge("infer_schema", "normalize_schema")     # normalize inferred schema
# graph.add_edge("normalize_schema", "build_execution_schema")
# graph.add_edge("build_execution_schema", "plan_batches")
# graph.add_edge("plan_batches", "generate")             # LLM data generation
# graph.add_edge("generate", "validate")                 # schema-driven validation
# graph.add_edge("validate", "write")                    # persist output
# graph.add_edge("write", END)

# # ----- Compile -----
# app = graph.compile()



# from langgraph.graph import StateGraph, END

# from app.nodes.intent_analyzer import analyze_intent
# from app.nodes.planner_agent import planner_agent
# from app.nodes.load_input_file import load_input_file
# from app.nodes.infer_schema_from_file import infer_schema_from_file
# from app.nodes.generator import generate_batches
# from app.nodes.write_output import write_output

# graph = StateGraph(dict)

# graph.add_node("intent", analyze_intent)
# graph.add_node("planner", planner_agent)
# graph.add_node("load_input", load_input_file)
# graph.add_node("infer_schema", infer_schema_from_file)
# graph.add_node("generate", generate_batches)
# graph.add_node("write", write_output)

# graph.set_entry_point("intent")

# graph.add_edge("intent", "planner")
# graph.add_edge("planner", "load_input")
# graph.add_edge("load_input", "infer_schema")
# graph.add_edge("infer_schema", "generate")
# graph.add_edge("generate", "write")
# graph.add_edge("write", END)

# app = graph.compile()

from langgraph.graph import StateGraph, END
from app.nodes import *
from app.nodes.intent import intent
from app.nodes.planner import planner
from app.nodes.tool_planner import tool_planner
from app.nodes.load_input import load_input
from app.nodes.infer_schema import infer_schema
from app.nodes.schema_fusion import schema_fusion
from app.nodes.build_execution_schema import build_execution_schema
from app.nodes.generator import generate
from app.nodes.validator import validate
from app.nodes.critic import critic
from app.nodes.write_output import write_output
g = StateGraph(dict)

g.add_node("intent", intent)
g.add_node("planner", planner)
g.add_node("tool_planner", tool_planner)
g.add_node("load_input", load_input)
g.add_node("infer_schema", infer_schema)
g.add_node("schema_fusion", schema_fusion)
g.add_node("build_exec", build_execution_schema)
g.add_node("generate", generate)
g.add_node("validate", validate)
g.add_node("critic", critic)
g.add_node("write", write_output)

g.set_entry_point("intent")

g.add_edge("intent", "planner")
g.add_edge("planner", "tool_planner")
g.add_edge("tool_planner", "load_input")
g.add_edge("load_input", "infer_schema")
g.add_edge("infer_schema", "schema_fusion")
g.add_edge("schema_fusion", "build_exec")
g.add_edge("build_exec", "generate")
g.add_edge("generate", "validate")
g.add_edge("validate", "critic")

g.add_conditional_edges("critic", lambda s: "generate" if s.get("retry") else "write")
g.add_edge("write", END)

app = g.compile()
