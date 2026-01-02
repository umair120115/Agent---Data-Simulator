from pathlib import Path

class FileSystemTool:
    def read_text(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8")

    def write_text(self, path: str, text: str):
        Path(path).write_text(text, encoding="utf-8")
