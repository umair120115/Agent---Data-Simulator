

# from app.tools.registry import tool_registry
# from app.tools.filesystem import FileSystemTool
# from app.tools.pdf_reader import PDFReaderTool
# from app.tools.json_writer import JSONWriterTool
# from app.tools.csv_writer import CSVWriterTool
# from app.tools.reasoning_logger import ReasoningLoggerTool

# tool_registry.register("filesystem", FileSystemTool())
# tool_registry.register("pdf_reader", PDFReaderTool())
# tool_registry.register("json_writer", JSONWriterTool())
# tool_registry.register("csv_writer", CSVWriterTool())
# tool_registry.register("reasoning_logger", ReasoningLoggerTool())


# app/tools/__init__.py
from app.tools.registry import tool_registry
from app.tools.filesystem import FileSystemTool
from app.tools.pdf_reader import PDFReaderTool
from app.tools.json_writer import JSONWriter
from app.tools.csv_writer import CSVWriter
from app.tools.text_writer import TextWriter
from app.tools.reasoning_logger import ReasoningLogger
from app.tools.memory import MemoryTool

tool_registry.register("filesystem", FileSystemTool())
tool_registry.register("pdf_reader", PDFReaderTool())
tool_registry.register("json_writer", JSONWriter())
tool_registry.register("csv_writer", CSVWriter())
tool_registry.register("text_writer", TextWriter())
tool_registry.register("reasoning_logger", ReasoningLogger())
tool_registry.register("memory", MemoryTool())
