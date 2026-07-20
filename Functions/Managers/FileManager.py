from pathlib import Path

SUPPORTED_FILES = {
    "pdf",
    "xlsx"
}

def get_file_type(file):
    return Path(file).suffix.lower().replace(".", "")

def support_file_extension(file: str) -> bool :
    return get_file_type(file) in SUPPORTED_FILES