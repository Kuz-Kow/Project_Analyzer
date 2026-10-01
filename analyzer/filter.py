from pathlib import Path
from typing import Iterator, Iterable
from analyze_models.data_models import FileInfo
import re


def filter_large(scanner : Iterable[Path], min_size : int) -> Iterator[Path]:
    for file in scanner:
        if isinstance(file, FileInfo):
            if file.size>= min_size:
                yield file
                

def filter_name(scanner : Iterable[Path], name : str) -> Iterator[Path]:
    for file in scanner:
        if isinstance(file, FileInfo):
            if re.match(f"{name}*", file.file_path.name):
                yield file