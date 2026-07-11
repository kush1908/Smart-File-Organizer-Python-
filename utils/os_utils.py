# os_utils.py
import os

def get_downloads_folder():
    return os.path.expanduser("~/Downloads")

def create_directory_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
