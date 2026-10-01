import logging
from typing import Iterator, TypedDict
from pathlib import Path
from collections import defaultdict
from analyze_models.data_models import Project_info, FileInfo



class Generator:
    """Generator object which caches return value of the scanner genarator"""

    def __init__(self, gen):
        self.gen = gen

    def __iter__(self):
        self.value = yield from self.gen
        return self.value


def analyze(scanner: Iterator[FileInfo]) -> Project_info:
    """
    Get's FileInfo objects from scanner and creates statistics of the whole project.
    """


    gen_scanner = Generator(scanner)

    analyzed_statistics = Project_info(Extensions=defaultdict(int))

    for file in gen_scanner:
        if isinstance(file, FileInfo):
            analyzed_statistics.Files += 1
            analyzed_statistics.Total_size += file.size
            analyzed_statistics.Extensions[file.suffix] += 1
            if len(analyzed_statistics.Largest_files.keys()) > 1:
                for value in sorted(analyzed_statistics.Largest_files):
                    if int(value) < file.size:
                        del analyzed_statistics.Largest_files[value]
                        analyzed_statistics.Largest_files[file.size] = (
                            file.file_path.name
                        )
                        break
            else:
                analyzed_statistics.Largest_files[file.size] = file.file_path.name

    analyzed_statistics.Directories = gen_scanner.value


    return analyzed_statistics
