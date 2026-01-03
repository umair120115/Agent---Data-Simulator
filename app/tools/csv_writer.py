# import csv
# from pathlib import Path

# class CSVWriterTool:
#     def write(self, path: str, rows):
#         if not rows:
#             return
#         Path(path).parent.mkdir(parents=True, exist_ok=True)
#         with open(path, "w", newline="", encoding="utf-8") as f:
#             writer = csv.DictWriter(f, fieldnames=rows[0].keys())
#             writer.writeheader()
#             writer.writerows(rows)
# app/tools/csv_writer.py
import csv
class CSVWriter:
    def write(self, path, data):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
