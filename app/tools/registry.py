# class ToolRegistry:
#     def __init__(self):
#         self._tools = {}

#     def register(self, name, tool):
#         self._tools[name] = tool

#     def get(self, name):
#         return self._tools[name]

# tool_registry = ToolRegistry()


class ToolRegistry:
    def __init__(self):
        self._tools = {}

    def register(self, name, tool):
        self._tools[name] = tool

    def get(self, name):
        if name not in self._tools:
            raise KeyError(f"Tool not registered: {name}")
        return self._tools[name]


tool_registry = ToolRegistry()
