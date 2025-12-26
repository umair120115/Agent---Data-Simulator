from app.tools import tool_registry
#to get the schema definition from the file excell may be 
def load_schema_definition(state: dict):
    fs = tool_registry.get("filesystem")
    definition = fs.load_excel_schema_definition(state["schema_definition_path"])

    return {
        **state,
        "schema_definition": definition
    }
