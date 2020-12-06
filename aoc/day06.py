from pathlib import Path

inputs = Path("files/day06.txt").read_text().strip()
groups = [line.split("\n") for line in inputs.split("\n\n")]


def part1():
    print(calc_sum([set("".join(group)) for group in groups]))


def part2():
    print(calc_sum([set(g[0]).intersection(*map(set, g[1:])) for g in groups]))


def calc_sum(answer_sets):
    answers = [len(answer_set) for answer_set in answer_sets]
    return sum(answers)


if __name__ == "__main__":
    part1()  # 6506
    part2()  # 3243
