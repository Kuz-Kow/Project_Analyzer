from pathlib import Path
from typing import Iterator, Iterable
import re

def filter_extension(scanner : Iterable[Path],extension : str) -> Iterator[Path]:
    for file in scanner:
        if file.is_file():
            if file.suffix == extension:
                yield file 

def filter_size(scanner : Iterable[Path], min_size : int) -> Iterator[Path]:
    for file in scanner:
        if file.is_file():
            if file.stat().st_size >= min_size:
                yield file
                

def filter_name(scanner : Iterable[Path], name : str) -> Iterator[Path]:
    for file in scanner:
        if file.is_file():
            if re.match(f"{name}*", file.name, re.IGNORECASE ):
                yield file