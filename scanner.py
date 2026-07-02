from pathlib import Path

def scan_folder(folder_path):
    files = []
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.is_file():
            files.append(file)

    return files