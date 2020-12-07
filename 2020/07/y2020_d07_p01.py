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



def can_contain(bags, bag):
    if bag == "shiny gold":
        return True

    for subbag in bags[bag]:
        if can_contain(bags, subbag):
            return True
        

    return False
        

for k in bags.keys():
    if k == "shiny gold":
        continue

    if can_contain(bags, k):
        ans += 1

print(ans)
