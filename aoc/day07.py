import re
from collections import defaultdict
from pathlib import Path


def parse_rule(r):
    subject, content_str = r.split(" contain ")
    content = content_str[:-1].split(", ")
    return subject, content


def build_set(rules):
    result = defaultdict(list)
    for subject, contents in rules:
        subject = subject.replace("bags", "bag")
        if contents[0] == "no other bags":
            result[subject] = []
            continue
        for content in contents:
            result[subject].append((content[0], content[2:].replace("bags", "bag")))
    return result


def find_options(rule_set, bag):
    results = []
    for subject, contents in rule_set.items():
        content = [content[1] for content in contents]
        if bag in content:
            results.append(subject)
            results = results + find_options(rule_set, subject)
    return list(set(results))


def find_contents(rule_set, bag):
    contents = rule_set[bag]
    return sum([int(content[0]) for content in contents]) + sum(
        [
            int(count) * find_contents(rule_set, content)
            for count, content in contents
            if rule_set[content]
        ]
    )
    return total


inputs = Path("files/day07.txt").read_text().strip().splitlines()
rules = [parse_rule(e) for e in inputs]
rule_set = build_set(rules)


def part1():
    print(len(find_options(rule_set, "shiny gold bag")))


def part2():
    print(find_contents(rule_set, "shiny gold bag"))


if __name__ == "__main__":
    part1()
    part2()
