
from .registry import tool_registry
from .filesystem import FileSystemTool
from .pdf_reader import PDFReaderTool
from .json_writer import JSONWriterTool

tool_registry.register("filesystem", FileSystemTool())
tool_registry.register("json_writer", JSONWriterTool())
tool_registry.register("pdf_reader", PDFReaderTool())
