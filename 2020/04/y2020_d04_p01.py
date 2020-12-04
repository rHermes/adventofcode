import fileinput
import re
import itertools as it

ans = 0
current_pass = []
for line in fileinput.input():
    line = line.rstrip()

    if line == "":
        if all([(x in current_pass) for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]):
            ans += 1
        current_pass = []

    for pair in line.split(" "):
        kk = pair.split(":")
        current_pass.append(kk[0])


if all([(x in current_pass) for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]):
    ans += 1
print(ans)
