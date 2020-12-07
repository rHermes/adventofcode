import fileinput
import itertools as it
import functools as fn
import re

# print(sum(len(set(x) - set("\n")) for x in "".join(fileinput.input()).split("\n\n")))

# for group in "".join(fileinput.input()).split("\n\n"):
#     print(group)
#     print()


ans = 0
bags = {}
for line in fileinput.input():
    line = line.rstrip()[:-1]
    bag, rst = line.split(" bags contain ")
    klt = {}
    if rst != "no other bags":
        for bb in rst.split(", "):
            aa = bb.split(" ")
            num = int(aa[0])
            name = " ".join(aa[1:-1])
            klt[name] = num

    bags[bag] = klt


def sum_up(bags, bag):
    ans = 0
    for subbag, num in bags[bag].items():
        ans += num * (sum_up(bags, subbag) + 1)

    return ans
        

print(sum_up(bags, "shiny gold"))
