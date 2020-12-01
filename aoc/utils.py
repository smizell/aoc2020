from pathlib import Path
from typing import List


def load_number_file(fp: Path) -> List[int]:
    with fp.open() as f:
        lines = f.readlines()
    return [int(line) for line in lines]
