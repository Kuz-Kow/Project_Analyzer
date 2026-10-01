from typing import NoReturn, Callable
from pathlib import Path
import argparse
from utils.processing import process_args
from config.setting import APP_NAME, VERSION, ACTIONS


def main() -> None:
    """
    Main function which gets parser and then get's args from parser and sends
    them to process_args function
    """
    parser = set_parser()
    args = vars(parser.parse_args())

    process_args(**args)


def set_parser() -> argparse.ArgumentParser:
    """
    Function which creates parser from template ACTION
    """

    parser = argparse.ArgumentParser(
        prog=APP_NAME + " " + VERSION,
        description="CLI application to analyze your project",
    )

    subpareser = parser.add_subparsers(
        required=True, dest="command", help="command to analyze your project"
    )

    for name, arguments in ACTIONS.items():
        p = subpareser.add_parser(name, help=arguments["help"])
        for argument in arguments["args"]:
            p.add_argument(argument.pop("name_or_flags"), **argument)

        p.add_argument("dir_path", help="Path to the project", type=Path)
        p.set_defaults(func=arguments["default_func"])

    return parser


if __name__ == "__main__":
    main()
