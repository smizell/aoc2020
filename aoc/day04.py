import re
from enum import Enum
from pathlib import Path
from typing import Optional
from pydantic import BaseModel, conint, ValidationError, validator


main_values = Path("files/day04.txt").read_text().split("\n\n")
pattern = r"(?P<key>\S+):(?P<value>\S+)"
passports = [dict(re.findall(pattern, values)) for values in main_values]


def part1():
    results = 0
    for passport in passports:
        try:
            Passport1(**passport)
            results += 1
        except:
            pass
    print(results)


def part2():
    results = 0
    for passport in passports:
        try:
            Passport2(**passport)
            results += 1
        except:
            pass
    print(results)


class EyeColor(Enum):
    AMB = "amb"
    BLU = "blu"
    BRN = "brn"
    GRY = "gry"
    GRN = "grn"
    HZL = "hzl"
    OTH = "oth"


class Passport1(BaseModel):
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[str] = None


class Passport2(Passport1):
    byr: conint(ge=1920, le=2002)
    iyr: conint(ge=2010, le=2020)
    eyr: conint(ge=2020, le=2030)
    ecl: EyeColor

    @validator("hgt")
    def valid_hgt(cls, hgt):
        """
        >>> Passport2.valid_hgt('60in')
        '60in'
        >>> Passport2.valid_hgt('190cm')
        '190cm'
        >>> Passport2.valid_hgt('190')
        Traceback (most recent call last):
        ValueError: Invalid hgt
        >>> Passport2.valid_hgt('190aa')
        Traceback (most recent call last):
        ValueError: Invalid hgt
        >>> Passport2.valid_hgt('190in')
        Traceback (most recent call last):
        ValueError: Invalid hgt
        >>> Passport2.valid_hgt('200cm')
        Traceback (most recent call last):
        ValueError: Invalid hgt
        """
        check = re.search(r"^(\d+)(in|cm)$", hgt)
        if not check:
            raise ValueError(f"Invalid hgt {hgt}")
        n, unit = check.groups()
        n = int(n)
        if unit == "in":
            if not (76 >= n >= 59):
                raise ValueError("Invalid hgt")
        if unit == "cm":
            if not (193 >= n >= 150):
                raise ValueError("Invalid hgt")
        return hgt

    @validator("hcl")
    def valid_hcl(cls, hcl):
        """
        >>> Passport2.valid_hcl('#123abc')
        '#123abc'
        >>> Passport2.valid_hcl('#123abz')
        Traceback (most recent call last):
        ValueError: Invalid hcl
        """
        if not re.search(r"^#[0-9a-f]{6}$", hcl):
            raise ValueError("Invalid hcl")
        return hcl

    @validator("pid")
    def valid_pid(cls, pid):
        """
        >>> Passport2.valid_pid('000000009')
        '000000009'
        >>> Passport2.valid_pid('1234')
        Traceback (most recent call last):
        ValueError: Invalid pid
        """
        if not re.search(r"^[0-9]{9}$", pid):
            raise ValueError("Invalid pid")
        return pid


if __name__ == "__main__":
    part1()  # 216
    part2()  # 150
