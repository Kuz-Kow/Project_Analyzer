from pathlib import Path
from analyzer.statistics import analyze
from analyzer.duplicates import find_duplicate
from analyzer.filter import filter_large, filter_name
from typing import TypedDict, Callable, Any

class action(TypedDict):
    help : str
    args : list[dict[str,Any]]
    default_func : Callable[...,Any]

 


DEFAULT_OUTPUT_DIR = Path("reports")

DEFAULT_OUTPUT_FILE_JSON = "analyze_report.json"

DEFAULT_OUTPUT_FILE_MARKDOWN = "analyze_report.md"

DEFAULT_LOG_DIR = Path("logs")

DEFAULT_LOG_FILE = DEFAULT_LOG_DIR / Path("app.log")

DEFAULT_MIN_SIZE = 1_000_000

SUPPORTED_REPORT_FORMATS = (
    "json",
    "md",
)

APP_NAME = "Project Analyzer"

VERSION = "1.0.0"


ACTIONS : dict[str, action] = {
    "analyze": {
        "help": "analyzes your project and prints it's statistics",
        "args": [],
        "default_func": analyze,
    },
    "large": {
        "args": [
            {
                "name_or_flags": "--min-size",
                "required": False,
                "default": DEFAULT_MIN_SIZE,
                "help": "Minimal size of the file in bytes to be considered large. Default: %(default)s",
                "dest": "min_size",
                "type": int,
            }
        ],
        "help": "Finds large files in your project",
        "default_func": filter_large,
    },
    "duplicates": {
        "args": [],
        "help": "Finds duplicates in your project",
        "default_func": find_duplicate,
    },
    "extensions": {
        "args": [],
        "help": "gives you statistics of all extensions in your project",
        "default_func": analyze,
    },
    "report": {
        "args": [
            {
                "name_or_flags": "--output",
                "required": True,
                "default": None,
                "dest": "output_file",
            }
        ],
        "help": "Creates a report about your project",
        "default_func": analyze,
    },
    "names": {
        "args": [{"name_or_flags": "name"}],
        "help": "find files by name",
        "default_func": filter_name,
    },
}
