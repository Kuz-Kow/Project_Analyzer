from typing import NoReturn
import argparse
from analyzer.scanner import dir_scanner as scanner
from analyzer.statistics import dir_statistics as statistics
from analyzer.duplicates import find_duplicate
from pathlib import Path
from config.setting import APP_NAME, VERSION, DEFAULT_MIN_SIZE

ACTIONS = {
    "analyze" : {"" :},
    "large" : {args : {name_or_flags : "--min-size",
                requaried : False,
                default : DEFAULT_MIN_SIZE,
                },
               help : {""}},
    "duolicates" : [],
    "extensions" : [],
    "report" : [{name_or_flags : "--output",
                 requaried : False,
                 default : None}]
}

def main() -> None:
    set_parser()
        

def set_parser():
    parser = argparse.ArgumentParser(prog= APP_NAME,
                                             description="CLI application to analyze your project",)
    
    subpareser = parser.add_subparsers(required=True)
    
    for name, arguments in ACTIONS:
        p = subpareser.add_parser(name, )
        
    
    subpareser = parser.add_subparsers(required=True)
    analyze_subparser = subpareser.add_parser("analyze")
    
    large_subparser = subpareser.add_parser("large")
    large_subparser.add_argument()
    
    subparser_names = []
    
    for action in parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            subparser_names = list(action.choices.keys()) 
            break
    
    for name in subparser_names:
        
        
    
    analyze_subparser.add_argument("dirpath", type= Path)
    

if __name__ == "__main__":
     main()