# app/tools/pdf_reader.py
from pypdf import PdfReader

class PDFReaderTool:
    def extract_text(self, path):
        reader = PdfReader(path)
        return "\n".join(p.extract_text() or "" for p in reader.pages)
