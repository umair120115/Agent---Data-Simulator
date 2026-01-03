# app/tools/text_writer.py
class TextWriter:
    def write(self, path, data):
        with open(path, "w", encoding="utf-8") as f:
            f.write(data if isinstance(data, str) else str(data))
