# app/tools/json_writer.py
import json
class JSONWriter:
    def write(self, path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
