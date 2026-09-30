from functools import lru_cache
from pathlib import Path
from typing import (Iterable)
from collections import defaultdict


@lru_cache
def hash_file(data: str):
    return hash(data)



def find_duplicate(scanner : Iterable[Path]) -> dict:
    
    hashed_files = defaultdict(list)
    duplicate_dict = {}
    groups = 0
    
    for file in scanner:
        if file.is_file():
            with file.open("r", encoding='latin-1') as file:
                hashed_files[hash(tuple(file.readlines()))].append(file)
    
    for value in hashed_files.values():
        if len(value) > 1:
            duplicate_dict[f"Group{groups+1}"] = value
    
    return duplicate_dict
    