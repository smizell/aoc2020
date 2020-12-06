from pathlib import Path

inputs = Path("files/day06.txt").read_text().strip()
groups = [line.split("\n") for line in inputs.split("\n\n")]


def part1():
    answer_sets = [set("".join(group)) for group in groups]
    print(calc_sum(answer_sets))


def part2():
    people_sets = [[set(person) for person in group] for group in groups]
    answer_sets = [
        set(people_set[0]).intersection(*people_set[1:]) for people_set in people_sets
    ]
    print(calc_sum(answer_sets))


def calc_sum(answer_sets):
    answers = [len(answer_set) for answer_set in answer_sets]
    return sum(answers)


if __name__ == "__main__":
    part1()  # 6506
    part2()  # 3243
