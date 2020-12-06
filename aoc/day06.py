from pathlib import Path

groups = [
    [set(g) for g in line.split("\n")]
    for line in Path("files/day06.txt").read_text().strip().split("\n\n")
]


if __name__ == "__main__":
    print(sum([len(set.union(*ps)) for ps in groups]))
    print(sum([len(set.intersection(*ps)) for ps in groups]))
