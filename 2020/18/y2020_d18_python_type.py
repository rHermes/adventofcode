# This is stolen from:
# https://github.com/CarletonComputerScienceSociety/advent-of-code-2020/blob/a1887ecebe5f95140de4de5e541c4d3efe38709d/2020/day-18/VictorLi5611/day18.py
#
# Just to showcase the fact that you can use python to do the parsing and
# evaluation for you. Absolutely filthy!
import fileinput as fi
import re
#https://www.guru99.com/python-regular-expressions-complete-tutorial.html 

class Operate(int):
    def __mul__(self, b):
        return Operate(int(self) + b)
    def __add__(self, b):
        return Operate(int(self) + b)
    def __sub__(self, b):
        return Operate(int(self) * b)

def solve1(expr):
    expr = re.sub(r"(\d+)", r"Operate(\1)", expr)
    expr = expr.replace("*", "-")
    return eval(expr, {}, {"Operate": Operate})

def solve2(expr):
    expr = re.sub(r"(\d+)", r"Operate(\1)", expr)
    expr = expr.replace("*", "-")
    expr = expr.replace("+", "*")
    return eval(expr, {}, {"Operate": Operate})


data = list(map(str.rstrip, fi.input()))
print("Part 1:", sum(map(solve1, data)))
print("Part 2:", sum(map(solve2, data)))
