from pathlib import Path
from typing import List


def load_number_file(fp: Path) -> List[int]:
    with fp.open() as f:
        lines = f.readlines()
    return [int(line) for line in lines]


def load_string_file(fp: Path) -> List[str]:
    with fp.open() as f:
        return f.readlines()
