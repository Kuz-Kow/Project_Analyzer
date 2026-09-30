import logging
from logger.logger_config import set_logger
from typing import (Iterator, TypedDict)
from pathlib import Path
from models.models import FileInfo
from collections import defaultdict

class Statistics_dict(TypedDict):
    Files : int
    Directories : int
    Extensions : defaultdict[str,int]
    Total_size : int
    Largest_files : dict[int, str]


set_logger()

logger = logging.getLogger(__name__)


class Generator:
    def __init__(self, gen):
        self.gen = gen
        
    def __iter__(self):
        self.value = yield from self.gen
        return self.value


def dir_statistics(scanner : Iterator[Path] ) -> dict:
    logger.info("Starting analysis")
    
    gen_scanner = Generator(scanner)
    
    analyzed_statistics : Statistics_dict = {
        "Files" : 0,
        "Directories" : 0,
        "Extensions" : defaultdict(int),
        "Total_size" : 0,
        "Largest_files" : {}        
    }
    
    for file in gen_scanner:
        if file.is_file():
            analyzed_statistics["Files"] += 1
            analyzed_statistics["Total_size"] += file.stat().st_size
            analyzed_statistics["Extensions"][file.suffix] += 1
            if len(analyzed_statistics["Largest_files"].keys()) > 1:
                for value in analyzed_statistics["Largest_files"]:
                    if int(value) < file.stat().st_size:
                        del  analyzed_statistics["Largest_files"][value]
                        analyzed_statistics["Largest_files"][file.stat().st_size] = file.name
                        break
            else:
                analyzed_statistics["Largest_files"][file.stat().st_size] = file.name
        
    analyzed_statistics["Directories"] = gen_scanner.value
    
    logger.info("Analyze finished")
    
    return analyzed_statistics
        
        
        
        