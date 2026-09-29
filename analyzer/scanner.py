import logging
import sys
from pathlib import Path
from typing import(Iterator)
from logger.logger_config import set_logger


set_logger()

logger = logging.getLogger(__name__)

def dir_scanner(dirpath: Path) -> Iterator[Path]:
    if dirpath.is_dir():
        directories = 0
        for obj in dirpath.rglob():
            if obj.is_dir():
                directories += 1
                dir_scanner(obj)
            yield obj
        return directories
    else:
        logger.error("Provided path doesn't directs to a directory")
        sys.exit()

    
