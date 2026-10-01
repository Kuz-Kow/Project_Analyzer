from pathlib import Path
from typing import Iterator, Iterable
from analyze_models.data_models import FileInfo
import re


def filter_large(scanner: Iterable[Path], min_size: int) -> Iterator[Path]:
    """
    Filtering large files in a project which a larger than min_size value
    """

    for file in scanner:
        if isinstance(file, FileInfo):
            if file.size >= min_size:
                yield file


def filter_name(scanner: Iterable[Path], name: str) -> Iterator[Path]:
    """
    Filtering fils by name using regular exprasion and yielding Path of the file
    """

    for file in scanner:
        if isinstance(file, FileInfo):
            if re.match(f"{name}*", file.file_path.name):
                yield file
