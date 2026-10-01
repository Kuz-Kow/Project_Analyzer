from pathlib import Path
import logging
from analyze_models.data_models import Project_info, FileInfo
from analyzer.scanner import dir_scanner
from config.setting import SUPPORTED_REPORT_FORMATS
import functools
from utils.helpers import create_json_report, create_markdown_report
from typing import Iterator


def process_args(*args, **kwargs):
    data_gen = dir_scanner(kwargs.pop("dir_path"))
    func = kwargs.pop("func")
    command = kwargs.pop("command")
    
    match command:
        case "analyze":
            result : Project_info = func(data_gen)
            print(f"Files: {result.Files}")
            print(f"Directories: {result.Directories}")
            print(f"Extensions: ")
            for extension, value in result.Extensions.items():
                print(f"  {extension} : {value}")
            print(f"Total size: {result.Total_size}")
            print(f"Larges file:")
            for size, name in result.Largest_files.items():
                print(f"   {name} : {size}")
            
        case "large":
            result : Iterator[FileInfo] = func(data_gen, *args, **kwargs)
            for file in result:
                print(f"{file.file_path.name} : {file.size} ")
                
        case "extensions" :
            result : Iterator[FileInfo] = func(*args, **kwargs)
            for extension, value in result.Extensions.items():
                    print(f"  {extension} : {value}")
                    
        case "report" :
            file = kwargs.pop("output_file")
            _ , suffix = file.split(".")
            if suffix in SUPPORTED_REPORT_FORMATS:
                result = func(data_gen,*args, **kwargs)
                if suffix == "json":
                    create_json_report(result, file)
                else:
                    create_markdown_report(result, file)
                    
        case "duplicates":
            result : dict[str, list[str]] = func(data_gen)
            for group, values in result.items():
                print(f"{group.capitalize()}:")
                for value in values:
                    print(f"   {value.name}")
                    
        case "names":
                result : Iterator[FileInfo] = func(data_gen, *args, **kwargs)
                for file in result:
                    print(f"\n{file.file_path.resolve()}\n")
            
                                
                    
            
                
                
    