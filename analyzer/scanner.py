import logging
import sys
from pathlib import Path
from typing import(Iterator)
from models.models import FileInfo
from logger.logger_config import set_logger


set_logger()

logger = logging.getLogger(__name__)

def dir_scanner(dirpath: Path) -> Iterator[FileInfo] | int:
    if dirpath.is_dir():
        directories = 0
        for obj in dirpath.rglob("**"):
            if obj.is_dir():
                directories += 1
            file_inf = FileInfo(file_path= obj,
                                suffix=obj.suffix,
                                size = obj.stat().st_size)
            yield file_inf
        return directories
    else:
        logger.error("Provided path doesn't directs to a directory")
        sys.exit()

    
