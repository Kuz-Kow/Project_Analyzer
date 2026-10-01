from pathlib import Path
import logging
from analyze_models.data_models import Project_info, FileInfo
from analyzer.scanner import dir_scanner
from config.setting import SUPPORTED_REPORT_FORMATS
from logger.logger_config import set_logger
import functools
import logging
from utils.helpers import create_json_report, create_markdown_report
from typing import Iterator, Callable

set_logger()

logger = logging.getLogger(__name__)

def process_args(*args, **kwargs) -> None:
    """
    Function to process all the args from parser and do needed operation
    """

    data_gen: Iterator[FileInfo] | int = dir_scanner(kwargs.pop("dir_path"))
    func: Callable = kwargs.pop("func")
    command: str = kwargs.pop("command")

    match command:
        case "analyze":
            logger.info("Started analysis")
            result: Project_info = func(data_gen)
            print(f"Files: {result.Files}")
            print(f"Directories: {result.Directories}")
            print(f"Extensions: ")
            for extension, value in result.Extensions.items():
                print(f"  {extension} : {value}")
            print(f"Total size: {result.Total_size}")
            print(f"Larges file:")
            for size, name in result.Largest_files.items():
                print(f"   {name} : {size}")
            logger.info("Ended analysis")

        case "large":
            large_result: Iterator[FileInfo] = func(data_gen, *args, **kwargs)
            for large_file in large_result:
                logger.info("Found large file: %s size: %s",large_file.file_path.name, large_file.size)
                print(f"{large_file.file_path.name} : {large_file.size} ")

        case "extensions":
            extensions_result: Project_info = func(*args, **kwargs)
            for extension, value in extensions_result.Extensions.items():
                print(f"  {extension} : {value}")

        case "report":
            file: str = kwargs.pop("output_file")
            _, suffix = file.split(".")
            if suffix in SUPPORTED_REPORT_FORMATS:
                report_result: Project_info = func(data_gen, *args, **kwargs)
                if suffix == "json":
                    create_json_report(report_result, file)
                else:
                    create_markdown_report(report_result, file)
                
                logger.info("Created report")

        case "duplicates":
            duplicates_result: dict[str, list[str]] = func(data_gen)
            for group, values in duplicates_result.items():
                print(f"{group.capitalize()}:")
                logger.info("Found duplicates: %s", values)
                for value in values:
                    print(f"   {value}")

        case "names":
            names_result: Iterator[FileInfo] = func(data_gen, *args, **kwargs)
            for named_file in names_result:
                print(f"\n{named_file.file_path.resolve()}\n")
