from pathlib import Path

DEFAULT_OUTPUT_DIR = Path("reports")

DEFAULT_OUTPUT_FILE_JSON = DEFAULT_OUTPUT_DIR / "analyze_report.json"

DEFAULT_OUTPUT_FILE_MARKDOWN = DEFAULT_OUTPUT_DIR / "analyze_report.md"

DEFAULT_LOG_DIR = Path("logs")

DEFAULT_LOG_FILE = DEFAULT_LOG_DIR / Path("app.log")

DEFAULT_MIN_SIZE = 1_000_000

SUPPORTED_REPORT_FORMATS = (
    "json",
    "markdown",
)

APP_NAME = "Project Analyzer"

VERSION = "1.0.0"