import operator
from functools import reduce
from pathlib import Path
from aoc.utils import load_string_file

lines = load_string_file(Path("files/day03.txt"))
matrix = [[char for char in line.strip()] for line in lines]

y_len = len(matrix)
x_len = len(matrix[0])


def part1():
    trees = find_trees(3, 1)
    print(trees)


def part2():
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    all_trees = [find_trees(*slope) for slope in slopes]
    total = reduce(operator.mul, all_trees)
    print(total)


def find_trees(x_slope, y_slope):
    trees = 0
    x = 0
    y = 0
    while True:
        x += x_slope
        y += y_slope
        if y > (y_len - 1):
            break
        if x > (x_len - 1):
            x = x - x_len
        if is_tree(matrix[y][x]):
            trees += 1
    return trees


def is_tree(char):
    return char == "#"


if __name__ == "__main__":
    part1()  # 167
    part2()  # 736527114
