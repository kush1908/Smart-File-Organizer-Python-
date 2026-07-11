# main.py
import os
from pathlib import Path
from utils.os_utils import get_downloads_folder
from utils.file_sorting import sort_files_by_extension
from utils.duplicate_finder import get_duplicates

def run():
    downloads_folder = get_downloads_folder()
    destination_folders = {
        "txt": "Text",
        "pdf": "Documents",
        "docx": "Word",
        "jpg": "Images",
        "png": "Images"
    }

    sort_files_by_extension(downloads_folder, destination_folders)
    duplicates = get_duplicates(downloads_folder)

    if duplicates:
        print("Duplicates found:")
        for duplicate in duplicates:
            print(duplicate)
    else:
        print("No duplicates found.")

if __name__ == "__main__":
    run()
