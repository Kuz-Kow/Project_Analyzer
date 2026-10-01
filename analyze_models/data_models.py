from dataclasses import dataclass, field
from pathlib import Path
from collections import defaultdict


@dataclass
class FileInfo:
    """
    Dataclass which contains needed information about file
    """

    file_path: Path
    suffix: str
    size: int


@dataclass
class Project_info:
    """
    Data class which containes whole information about project
    """

    Files: int = field(default=0)
    Directories: int = field(default=0)
    Extensions: defaultdict = field(default_factory=defaultdict)
    Total_size: int = 0
    Largest_files: dict = field(default_factory=dict)
