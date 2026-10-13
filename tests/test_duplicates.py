from pathlib import Path

from analyze_models.data_models import FileInfo
from analyzer.duplicates import find_duplicate


def test_find_duplicate(tmp_path: Path) -> None:
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file3 = tmp_path / "file3.txt"

    file1.write_text("Hello world\n", encoding="utf-8")
    file2.write_text("Hello world\n", encoding="utf-8")
    file3.write_text("Different content\n", encoding="utf-8")

    scanner = [
        FileInfo(file_path=file1,suffix=file1.suffix ,size=file1.stat().st_size),
        FileInfo(file_path=file2, suffix=file2.suffix, size=file2.stat().st_size),
        FileInfo(file_path=file3, suffix=file3.suffix, size=file3.stat().st_size),
    ]

    result = find_duplicate(scanner)

    assert len(result) == 1

    duplicate_paths = next(iter(result.values()))

    assert len(duplicate_paths) == 2
    assert file1.resolve() in duplicate_paths
    assert file2.resolve() in duplicate_paths
    assert file3.resolve() not in duplicate_paths