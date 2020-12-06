from pathlib import Path

inputs = Path("files/day06.txt").read_text().strip()
groups = [line.split("\n") for line in inputs.split("\n\n")]
group_sets = [list(map(set, g)) for g in groups]


if __name__ == "__main__":
    print(sum([len(set.union(*g)) for g in group_sets]))
    print(sum([len(set.intersection(*g)) for g in group_sets]))
