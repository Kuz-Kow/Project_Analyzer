from typing import NoReturn
import argparse
from analyzer.scanner import dir_scanner as scanner
from analyzer.statistics import dir_statistics as statistics
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(prog= "Project Analyzer",
                                         description="CLI application to analyze your project")
        
    subpareser = parser.add_subparsers(required=True)
    analyze_subparser = subpareser.add_parser("analyze")
    analyze_subparser.add_argument("dirpath", type= Path)
    
    args = parser.parse_args()
    
    dir_scanner = scanner(args.dirpath)
    
    stats = statistics(dir_scanner)
    
    for name, value in stats.items():
        print(f"{name} : {value}")
        



if __name__ == "__main__":
     main()