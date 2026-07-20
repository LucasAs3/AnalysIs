import pymupdf
import pathlib

def pdf_reader(file: str) -> str:
    with pymupdf.open(file) as doc:
        text = chr(12).join([page.get_text() for page in doc])
    
    return text