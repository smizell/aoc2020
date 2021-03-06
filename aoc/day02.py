import re
from collections import Counter
from pathlib import Path
from aoc.utils import load_string_file

PATTERN = r"(?P<n1>\d+)-(?P<n2>\d+) (?P<letter>\w): (?P<password>\w+)"
lines = load_string_file(Path("files/day02.txt"))
parsed = [re.search(PATTERN, line).groupdict() for line in lines]  # type: ignore


def part1():
    validated = (validate_part1(line) for line in parsed)
    total = len(list(filter(bool, validated)))
    print("part1", total)


def validate_part1(check):
    counter = Counter(check["password"])
    letter_count = counter[check["letter"]]
    return True if int(check["n2"]) >= letter_count >= int(check["n1"]) else False


def part2():
    validated = (validate_part2(line) for line in parsed)
    total = len(list(filter(bool, validated)))
    print("part2", total)


def validate_part2(check):
    idx1 = int(check["n1"]) - 1
    idx2 = int(check["n2"]) - 1
    return (
        True
        if (
            check["letter"] == check["password"][idx1]
            or check["letter"] == check["password"][idx2]
        )
        and check["password"][idx1] != check["password"][idx2]
        else False
    )


if __name__ == "__main__":
    part1()  # 434
    part2()  # 509
