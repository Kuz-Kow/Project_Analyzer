from pathlib import Path
from typing import Iterator, Iterable
from analyze_models.data_models import FileInfo
import re


def filter_large(scanner: Iterable[FileInfo], min_size: int) -> Iterator[FileInfo]:
    """
    Filtering large files in a project which a larger than min_size value
    """

    for file in scanner:
        if isinstance(file, FileInfo):
            if file.size >= min_size:
                yield file


def filter_name(scanner: Iterable[FileInfo], name: str) -> Iterator[FileInfo]:
    """
    Filtering fils by name using regular exprasion and yielding Path of the file
    """

    for file in scanner:
        if isinstance(file, FileInfo):
            if re.match(f"{name}*", file.file_path.name):
                yield file
