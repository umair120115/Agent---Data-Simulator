class ToolRegistry:
    def __init__(self):
        self._tools = {}

    def register(self, name, tool):
        self._tools[name] = tool

    def get(self, name):
        return self._tools[name]

tool_registry = ToolRegistry()
