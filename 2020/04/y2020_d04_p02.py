import fileinput
import re
import itertools as it

def valid(p):
    if not all([(x in c) for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]):
        return False

    if len(p["pid"]) != 9 or not p["pid"].isnumeric():
        return False
    
    if len(p["byr"]) != 4 or not p["byr"].isnumeric() or not (1920 <= int(p["byr"]) <= 2002):
        return False

    if len(p["iyr"]) != 4 or not p["iyr"].isnumeric() or not (2010 <= int(p["iyr"]) <= 2020):
        return False

    if len(p["eyr"]) != 4 or not p["eyr"].isnumeric() or not (2020 <= int(p["eyr"]) <= 2030):
        return False

    if not (p["hgt"].endswith("cm") or p["hgt"].endswith("in")):
        return False

    if p["hgt"][-2:] == "cm":
        if not (150 <= int(p["hgt"][:-2]) <= 193):
            return False
    elif p["hgt"][-2:] == "in":
        if not (59 <= int(p["hgt"][:-2]) <= 76):
            return False
    else:
        return False

    hcl = p["hcl"]

    if hcl[0] != '#' or len(hcl) != 7 or not all([x in "0123456789abcdef" for x in hcl[1:]]):
        return False

    if p["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    
    return True

    
ans = 0
c = {}
for line in fileinput.input():
    line = line.rstrip()

    if line == "":
        if valid(c):
            ans += 1

        c = {}

    for pair in line.split(" "):
        kk = pair.split(":")
        c[kk[0]] = ":".join(kk[1:])

if valid(c):
    ans += 1

print(ans)
