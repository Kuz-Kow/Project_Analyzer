# Project Analyzer

**Project Analyzer** is a lightweight command-line tool for analyzing the structure and basic statistics of a software project.

It recursively scans a project directory and provides information about files, directories, file extensions, total project size, large files, duplicate files, and files matching a specified name pattern. Reports can also be exported to **JSON** or **Markdown**.

## Features

* 📊 Analyze project statistics

  * Number of files
  * Number of directories
  * File extension distribution
  * Total project size
  * Largest files
* 📦 Find large files with a configurable size threshold
* 🔁 Find duplicate files
* 🔎 Find files by name using a regular expression
* 📄 Generate reports in:

  * JSON
  * Markdown
* 📝 Application logging with rotating log files
* 🐍 Written in Python using the standard library

## Project Structure

```text
Project_Analyzer/
├── analyze_models/
│   └── data_models.py       # Data models for files and project statistics
│
├── analyzer/
│   ├── duplicates.py        # Duplicate file detection
│   ├── filter.py            # File filtering utilities
│   ├── scanner.py           # Recursive project scanner
│   └── statistics.py        # Project statistics calculation
│
├── config/
│   └── setting.py           # Application configuration and CLI commands
│
├── logger/
│   └── logger_config.py     # Logging configuration
│
├── utils/
│   ├── helpers.py           # JSON and Markdown report generation
│   └── processing.py        # CLI argument processing
│
├── ProjectAnalyzer.py       # CLI entry point
├── LICENSE
└── README.md
```

The scanner represents every discovered file as a `FileInfo` object containing its path, extension, and size. Project-wide results are stored in a `Project_info` data model.

## Requirements

* Python **3.10+**
* No external Python packages are required.

The project relies on modules from the Python standard library such as `argparse`, `pathlib`, `logging`, `dataclasses`, `json`, and `re`.

## Installation

Clone the repository:

```bash
git clone https://github.com/Kuz-Kow/Project_Analyzer.git
cd Project_Analyzer
```

No dependency installation is required.

You can verify that the CLI is available with:

```bash
python ProjectAnalyzer.py --help
```

## Usage

The general command format is:

```bash
python ProjectAnalyzer.py <command> <project_path>
```

### Analyze a project

The `analyze` command displays general project statistics:

```bash
python ProjectAnalyzer.py analyze .
```

Example output:

```text
Files: 42
Directories: 8
Extensions:
  .py : 25
  .md : 4
  .json : 3
  .txt : 2
Total size: 184320
Larges file:
   example.py : 42100
   data.json : 31500
```

The analysis counts files and directories recursively and groups files by their extension.

### Find large files

Use the `large` command to find files larger than a specified size.

By default, the threshold is **1,000,000 bytes**.

```bash
python ProjectAnalyzer.py large .
```

Specify your own threshold with `--min-size`:

```bash
python ProjectAnalyzer.py large --min-size 500000 .
```

The value is specified in bytes.

For example:

```bash
python ProjectAnalyzer.py large --min-size 1048576 .
```

will find files that are at least 1 MiB in size.

### Find duplicate files

The `duplicates` command searches the project for files with identical contents:

```bash
python ProjectAnalyzer.py duplicates .
```

Example:

```text
Group1:
   /project/config/example.json
   /project/tests/example.json

Group2:
   /project/data/sample.txt
   /project/docs/sample.txt
```

Duplicate detection currently compares the contents of files and groups files with matching content.

### Find files by name

The `names` command searches for files using a name pattern:

```bash
python ProjectAnalyzer.py names config .
```

The search is performed against the file name using Python regular expressions.

For example:

```bash
python ProjectAnalyzer.py names ".*test.*" .
```

can be used to find files whose names contain `test`.

### Generate a report

Reports can be generated in JSON or Markdown format.

#### JSON

```bash
python ProjectAnalyzer.py report --output report.json .
```

#### Markdown

```bash
python ProjectAnalyzer.py report --output report.md .
```

The application supports the following report formats:

```text
.json
.md
```

Generated reports are stored in the `reports/` directory.

A JSON report contains information such as:

```json
{
  "files": 42,
  "directories": 8,
  "extensions": {
    ".py": 25,
    ".md": 4,
    ".json": 3
  },
  "total_size": 184320,
  "largest_files": {
    "42100": "example.py"
  }
}
```

Markdown reports contain the same basic information in a human-readable format.

## Logging

Project Analyzer uses Python's built-in `logging` module.

Logs are written to:

```text
logs/app.log
```

The application uses a rotating log file with a maximum size of 1000 bytes and keeps up to 10 backup files. Errors are also displayed in the console.

## How It Works

The analysis pipeline is relatively simple:

```text
Project directory
       │
       ▼
   Directory
    Scanner
       │
       ▼
    FileInfo
    objects
       │
       ├───────────────┐
       ▼               ▼
   Statistics      File Filters
       │               │
       │         ┌─────┴─────┐
       │         ▼           ▼
       │       Large      Name Search
       │       Files
       │
       ├───────────────┐
       ▼               ▼
    Console         Reports
                    │
              ┌─────┴─────┐
              ▼           ▼
             JSON       Markdown
```

The scanner recursively walks through the supplied directory using `pathlib.Path.rglob()` and creates `FileInfo` objects for discovered files.

## Configuration

Default application settings are located in:

```text
config/setting.py
```

Important defaults include:

| Setting              | Default               |
| -------------------- | --------------------- |
| Application name     | `Project Analyzer`    |
| Version              | `1.0.0`               |
| Report directory     | `reports/`            |
| JSON report          | `analyze_report.json` |
| Markdown report      | `analyze_report.md`   |
| Log directory        | `logs/`               |
| Large file threshold | `1,000,000` bytes     |

The CLI currently provides the following commands: `analyze`, `large`, `duplicates`, `extensions`, `report`, and `names`.

## Development

The project is organized into small modules with separate responsibilities:

* `scanner.py` — discovers files and directories
* `statistics.py` — calculates project statistics
* `duplicates.py` — detects duplicate files
* `filter.py` — provides file filtering operations
* `data_models.py` — defines data structures
* `helpers.py` — generates reports
* `processing.py` — connects CLI arguments with analysis functions
* `ProjectAnalyzer.py` — application entry point

This structure makes individual analysis components relatively easy to extend or replace.

## Known Limitations

The current implementation is intentionally lightweight and has several limitations:

* The scanner processes every file under the supplied directory and does not currently provide ignore rules for directories such as `.git`, `venv`, `node_modules`, or `__pycache__`.
* Duplicate detection reads file contents using `latin-1` and uses Python's built-in `hash()` rather than a cryptographic hash.
* Report generation expects the `reports/` directory to be available.
* The `extensions` command is present in the CLI configuration but its current argument-processing path should be reviewed before relying on it.
* File-name matching uses regular expressions, so special regex characters in a search pattern may affect the result.

These are implementation characteristics of the current `main` branch rather than requirements of the project.

## License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for the full license text. The repository's license identifies the copyright holder as Andrii and uses the standard MIT terms.

## Author

**Andrii**

Repository:

https://github.com/Kuz-Kow/Project_Analyzer
