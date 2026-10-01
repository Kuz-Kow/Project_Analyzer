from functools import lru_cache
from pathlib import Path
from typing import Iterable
from analyze_models.data_models import FileInfo
from collections import defaultdict


@lru_cache
def hash_file(data: str):
    """Creating hash of the data"""
    return hash(data)


def find_duplicate(scanner: Iterable[Path]) -> dict[str, list[Path]]:
    """
    Finding duplicates of some files in project.
    Retorning groups of the same file
    """
    hashed_files = defaultdict(list)
    duplicate_dict = {}
    groups = 0

    for file in scanner:
        if isinstance(file, FileInfo):
            with file.file_path.open("r", encoding="latin-1") as file_reading:
                hashed_files[hash(tuple(file_reading.readlines()))].append(
                    file.file_path.resolve()
                )

    for values in hashed_files.values():
        if len(values) > 1:
            duplicate_dict[f"Group{groups+1}"] = values

    return duplicate_dict
