import itertools
import operator
from functools import reduce
from pathlib import Path
from aoc.utils import load_number_file
from typing import List, Tuple

nums = load_number_file(Path("files/day01.txt"))


def find_match(nums: List[int], looking_for: int, matches: int) -> List[int]:
    """
    >>> nums = [1721, 979, 366, 299, 675, 1456]
    >>> find_match(nums, looking_for=2020, matches=2)
    [1721, 299]
    >>> find_match(nums, looking_for=2020, matches=3)
    [979, 366, 675]
    >>> find_match([1,2], looking_for=1000, matches=2)
    []
    """
    search_nums = (nums[l:] for l in range(matches))
    results = (
        list(values)
        for values in itertools.product(*search_nums)
        if sum(values) == looking_for
    )
    return next(results, [])


if __name__ == "__main__":
    result1 = reduce(operator.mul, find_match(nums, looking_for=2020, matches=2))
    result2 = reduce(operator.mul, find_match(nums, looking_for=2020, matches=3))
    print("part1", result1)
    print("part2", result2)
    # part1 1009899
    # part2 44211152
