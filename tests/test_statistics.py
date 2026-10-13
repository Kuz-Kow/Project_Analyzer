import pytest
from typing import Iterable
from pathlib import Path
from analyzer.statistics import analyze
from analyze_models.data_models import FileInfo, Project_info
from collections import defaultdict

scanner : list[FileInfo | int]= [
    FileInfo(Path("python.py"),
             ".py",
             1000),
    FileInfo(Path("direc/pyt.py"),
                ".py",
                200),
    FileInfo(Path("files.txt"),
            ".txt",
            900),
    FileInfo(Path("dirs/settings/set.json"),
            ".json",
            10000),
    FileInfo(Path("dirs/settings/new.json"),
                ".json",
                20000),
    FileInfo(Path("dirs/test.py"),
                ".py",
                12000),
    4]

def test_scanner() -> Iterable[FileInfo] | int:
    
    dirs = 0
    
    for value in scanner:
        dirs = value
        yield value
        
    return dirs




def test_statistics():
    statistic_analyzer = analyze(scanner= test_scanner())
    
    assert statistic_analyzer == Project_info(Files= 6,
                                              Directories= 4,
                                              Extensions= defaultdict(**{".py" : 3, ".json" : 2, ".txt" : 1}),
                                              Total_size = 44100,
                                              Largest_files = {
                                                20000 : "new.json",
                                                12000 : "test.py"
                                              })
