# app/tools/filesystem.py
from pathlib import Path

class FileSystemTool:
    def read_text(self, path):
        return Path(path).read_text(errors="ignore")
