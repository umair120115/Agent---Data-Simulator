# app/tools/memory.py
import json
from pathlib import Path

class MemoryTool:
    def __init__(self, path="agent_memory.json"):
        self.path = Path(path)
        if not self.path.exists():
            self.path.write_text("{}")

    def read(self):
        return json.loads(self.path.read_text())

    def write(self, data):
        self.path.write_text(json.dumps(data, indent=2))
