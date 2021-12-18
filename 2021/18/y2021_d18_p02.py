import fileinput as fi
import itertools as it
import functools as ft
import math
from ast import literal_eval

# Inspired/stolen from: https://github.com/benediktwerner/AdventOfCode/blob/master/2021/day18/sol.py

def add_to(x, n, left):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    if left:
        return (add_to(x[0], n, left), x[1])
    else:
        return (x[0], add_to(x[1], n, left))

# returns: changed, left, exp, right
def explode(x, n=4):
    if isinstance(x, int):
        return False, None, x, None

    if n == 0:
        return True, x[0], 0, x[1]

    a, b = x
    change, left, a, right = explode(a, n - 1)
    if change:
        return True, left, (a, add_to(b, right, left=True)), None

    change, left, b, right = explode(b, n - 1)
    if change:
        return True, None, (add_to(a, left, left=False), b), right

    return False, None, x, None

# Returns changed, x
def split(x):
    if isinstance(x, int):
        if 10 <= x:
            return True, (x // 2, math.ceil(x / 2))
        return False, x

    a, b = x

    change, a = split(a)
    if change:
        return True, (a, b)

    change, b = split(b)
    return change, (a, b)


def sadd(a, b):
    x = (a, b)
    while True:
        change, _, x, _ = explode(x)
        if change:
            continue

        change, x = split(x)
        if not change:
            break

    return x

def mag(x):
    if isinstance(x, int):
        return x

    return 3 * mag(x[0]) + 2 * mag(x[1])


def solve(numbers):
    return max(mag(sadd(a,b)) for a, b in it.permutations(numbers, r=2))

# I want tuples, not lists, so I am sure they are immutable
tr = str.maketrans("[]", "()")
numbers = [literal_eval(x.rstrip().translate(tr)) for x in fi.input()]
print(solve(numbers))
