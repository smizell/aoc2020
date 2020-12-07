import re
from collections import defaultdict
from pathlib import Path


def parse_rule(r):
    subject, content_str = r.split(" contain ")
    content = content_str[:-1].split(", ")
    return subject, content


def build_set(rules):
    def normalize_bag_name(bag_name):
        return bag_name.replace("bags", "bag")

    result = defaultdict(list)
    for subject, contents in rules:
        subject = normalize_bag_name(subject)
        if contents[0] == "no other bags":
            result[subject] = []
            continue
        for content in contents:
            result[subject].append((int(content[0]), normalize_bag_name(content[2:])))
    return result


inputs = Path("files/day07.txt").read_text().strip().splitlines()
rules = [parse_rule(e) for e in inputs]
rule_set = build_set(rules)


def find_options(rule_set, bag):
    results = []
    for subject, contents in rule_set.items():
        bags = [content for _, content in contents]
        if bag not in bags:
            continue
        results += [subject] + find_options(rule_set, subject)
    return list(set(results))


def find_contents(rule_set, bag):
    contents = rule_set[bag]
    return sum([count for count, _ in contents]) + sum(
        [
            count * find_contents(rule_set, content)
            for count, content in contents
            if rule_set[content]
        ]
    )
    return total


def part1():
    print(len(find_options(rule_set, "shiny gold bag")))


def part2():
    print(find_contents(rule_set, "shiny gold bag"))


if __name__ == "__main__":
    part1()
    part2()
