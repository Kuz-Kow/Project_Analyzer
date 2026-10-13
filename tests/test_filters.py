import pytest
from pathlib import Path
from analyze_models.data_models import FileInfo
from analyzer.filter import filter_large, filter_name


scanner = [
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


    ]


def test_filter_large():
    large_file_filter = filter_large(scanner = scanner,
                                 min_size= 1000)
    
    
    assert next(large_file_filter) == FileInfo(Path("python.py"), ".py", 1000)
    assert next(large_file_filter) == FileInfo(Path("dirs/settings/set.json"), ".json", 10000)
    with pytest.raises(StopIteration):
        next(large_file_filter)
        
        

def test_filter_name():
    name_file_scanner = filter_name(scanner= scanner,
                                    name= "pyt")
    
    assert next(name_file_scanner) == FileInfo(Path("python.py"), ".py", 1000)
    assert next(name_file_scanner) == FileInfo(Path("direc/pyt.py"), ".py", 200)
    
    with pytest.raises(StopIteration):
        next(name_file_scanner)