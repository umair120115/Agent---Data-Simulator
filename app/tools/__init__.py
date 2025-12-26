from app.tools.registry import ToolRegistry
from app.tools.filesystem import FileSystemTool
from app.tools.math_tool import MathTool

tool_registry = ToolRegistry()
tool_registry.register("filesystem", FileSystemTool())
tool_registry.register("math", MathTool())
