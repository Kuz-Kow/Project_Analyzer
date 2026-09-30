import json
from pathlib import Path
import logging
from analyze_models.data_models import Project_info
from config.setting import DEFAULT_OUTPUT_FILE_JSON, DEFAULT_OUTPUT_FILE_MARKDOWN
from logger.logger_config import set_logger

set_logger()

logger = logging.getLogger(__name__)

def create_json_report(report : Project_info) -> None:
    statistic_dict = {
        "files" : report.Files,
        "directories" : report.Directories,
        "extensions" : report.Extensions,
        "total_size" : report.Total_size,
        "largest_files" : report.Largest_files
    }
    
    with DEFAULT_OUTPUT_FILE_JSON.open("w") as file:
        json.dump(statistic_dict, file, indent = 2)
        logger.info("Created json report in in path: %s", DEFAULT_OUTPUT_FILE_JSON.resolve())
    


def create_markdown_report(report : Project_info) -> None:
    with DEFAULT_OUTPUT_FILE_MARKDOWN.open("w") as file:
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

