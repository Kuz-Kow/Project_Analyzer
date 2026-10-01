import json
from pathlib import Path
import logging
from analyze_models.data_models import Project_info
from config.setting import (
    DEFAULT_OUTPUT_FILE_JSON,
    DEFAULT_OUTPUT_FILE_MARKDOWN,
    DEFAULT_OUTPUT_DIR,
)
from logger.logger_config import set_logger

set_logger()

logger = logging.getLogger(__name__)


def create_json_report(
    report: Project_info, filename: str = DEFAULT_OUTPUT_FILE_JSON
) -> None:
    """
    Creates json report from Project_info object and saves it in reports folder.
    Takes filename from user if not provided uses default name
    """

    file: Path = Path(DEFAULT_OUTPUT_DIR / Path(filename))

    statistic_dict: dict[str, str | dict | int] = {
        "files": report.Files,
        "directories": report.Directories,
        "extensions": report.Extensions,
        "total_size": report.Total_size,
        "largest_files": report.Largest_files,
    }

    with file.open("w") as save:
        json.dump(statistic_dict, save, indent=2)
        logger.info("Created json report in in path: %s", file.resolve())


def create_markdown_report(
    report: Project_info, filename: str = DEFAULT_OUTPUT_FILE_MARKDOWN
) -> None:
    """
    Creates markdown report from Project_info object and saves it in reports folder.
    Takes filename from user if not provided uses default name
    """

    write_file = Path(DEFAULT_OUTPUT_DIR / Path(filename))

    with write_file.open("w") as file:
        file.write("## Analyze result\n")
        file.write(f"### Files: {report.Files}\n")
        file.write(f"### Directories: {report.Directories}\n")
        file.write(f"### Extensions:\n")
        for extension, value in report.Extensions.items():
            file.write(f"   - {extension} : {value}\n")
        file.write(f"### Total size: {report.Total_size}\n")
        file.write("### Largest files:\n")
        for file_size, file_name in report.Largest_files.items():
            file.write(f"   - {file_name} : {file_size}\n")
