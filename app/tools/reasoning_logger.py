# from datetime import datetime
# from pathlib import Path

# class ReasoningLoggerTool:
#     def __init__(self, path="agent_reasoning.txt"):
#         self.path = Path(path)

#     def log(self, message: str):
#         timestamp = datetime.utcnow().isoformat()
#         self.path.parent.mkdir(parents=True, exist_ok=True)
#         with open(self.path, "a", encoding="utf-8") as f:
#             f.write(f"[{timestamp}] {message}\n")

# app/tools/reasoning_logger.py
from datetime import datetime

class ReasoningLogger:
    def __init__(self, path="agent_reasoning.txt"):
        self.path = path

    def log(self, msg):
        with open(self.path, "a") as f:
            f.write(f"[{datetime.utcnow()}] {msg}\n")
