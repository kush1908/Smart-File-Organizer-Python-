# duplicate_finder.py
import hashlib
import os
from typing import List

def get_duplicates(downloads_folder: str) -> List[str]:
    duplicates = []
    seen_hashes = set()

    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        with open(file_path, "rb") as f:
            content = f.read()
            hash_value = hashlib.sha256(content).hexdigest()

            if hash_value in seen_hashes:
                duplicates.append(file_path)
            else:
                seen_hashes.add(hash_value)

    return duplicates
