import fileinput
from functools import lru_cache, reduce

BAGS = {}
for line in fileinput.input():
    bag, rst = line.rstrip()[:-1].split(" bags contain ")
    cons = {}
    if rst != "no other bags":
        for obags in rst.split(", "):
            xs = obags.split(" ")
            cons[" ".join(xs[1:-1])] = int(xs[0])

    BAGS[bag] = cons

# We use dynamic programming here, to avoid recomputing values
# we have previously computed
@lru_cache(None)
def sum_up(bag):
    return sum(n * (sum_up(b)+1) for (b,n) in BAGS[bag].items())

print(sum_up("shiny gold"))
