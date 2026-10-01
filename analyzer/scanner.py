import logging
import sys
from pathlib import Path
from typing import Iterator
from analyze_models.data_models import FileInfo
from logger.logger_config import set_logger

set_logger()

logger = logging.getLogger(__name__)


def dir_scanner(dirpath: Path) -> Iterator[FileInfo] | int:
    """
    Scanns whole project yileds all files and returns amount of the directories
    """

    if dirpath.is_dir():
        directories: int = 0
        for obj in dirpath.rglob("**"):
            if obj.is_dir():
                directories += 1
                continue
            file_inf = FileInfo(
                file_path=obj, suffix=obj.suffix, size=obj.stat().st_size
            )
            yield file_inf
        return directories
    else:
        logger.error("Provided path doesn't directs to a directory")
        sys.exit()
