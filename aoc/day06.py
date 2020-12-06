from pathlib import Path

inputs = Path("files/day06.txt").read_text().strip()
groups = [line.split("\n") for line in inputs.split("\n\n")]


if __name__ == "__main__":
    print(sum([len(set.union(*map(set, g))) for g in groups]))
    print(sum([len(set.intersection(*map(set, g))) for g in groups]))
