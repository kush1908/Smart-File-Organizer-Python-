# file_sorting.py
import pathlib
from typing import List

def get_extensions():
    return ["txt", "pdf", "docx", "jpg", "png"]

def sort_files_by_extension(downloads_folder: str, destination_folders: dict):
    for ext in get_extensions():
        dest_path = os.path.join(destination_folders[ext], ext)
        create_directory_if_not_exists(dest_path)
        source_path = os.path.join(downloads_folder, f"*.{ext}")
        shutil.move(source_path, dest_path)
