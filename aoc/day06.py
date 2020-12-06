from pathlib import Path

inputs = Path("files/day06.txt").read_text().strip()
groups = [line.split("\n") for line in inputs.split("\n\n")]


if __name__ == "__main__":
    print(sum([len(set("".join(group))) for group in groups]))
    print(sum([len(set(g[0]).intersection(*map(set, g[1:]))) for g in groups]))
