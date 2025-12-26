import json
import pandas as pd
from pathlib import Path

class FileSystemTool:

    def _resolve(self, path):
        p = Path(path).expanduser()
        if not p.is_absolute():
            p = Path.cwd() / p
        return p

    def load_json(self, path):
        with open(self._resolve(path), "r", encoding="utf-8") as f:
            return json.load(f)

    def load_excel_schema_definition(self, path):
        df = pd.read_excel(self._resolve(path))
        result = {}

        for _, row in df.iterrows():
            result[row["Element Name"]] = {
                "type": row["Data Type"],
                "description": row["Description"]
            }

        return result

