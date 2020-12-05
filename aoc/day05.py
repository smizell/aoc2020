import math
from collections import defaultdict
from pathlib import Path
from aoc.utils import load_string_file

lines = load_string_file(Path("files/day05.txt"))


def part1():
    results = [handle_instructions(i.strip()) for i in lines]
    ids = [(row * 8) + column for row, column in results]
    print(max(ids))


def part2():
    results = [handle_instructions(i.strip()) for i in lines]
    ids = sorted([(row * 8) + column for row, column in results])
    next([b - 1 for a, b in zip(ids, ids[1:]) if b - a == 2])


def handle_instructions(instructions):
    """
    >>> handle_instructions('BFFFBBFRRR')
    (70, 7)
    """
    row_instructions = instructions[0:7]
    column_instructions = instructions[7:10]
    row = bisect(row_instructions, (0, 127), "F", "B")
    column = bisect(column_instructions, (0, 7), "L", "R")
    return row, column


def bisect(instructions, current, l_char, u_char):
    for i in instructions:
        lower, upper = current
        if i == l_char:
            current = (lower, int(len(range(lower, upper)) / 2) + lower)
        if i == u_char:
            current = (lower + int((len(range(lower, upper)) / 2)) + 1, upper)
    return current[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    part1()  # 896
    part2()  # 659
