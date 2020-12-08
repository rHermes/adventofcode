import fileinput
import functools as ft
import itertools as it
import more_itertools as mit

# findall
# parse
# search

from parse import *

prog = []
for line in fileinput.input():
    line = line.rstrip()
    if line == "":
        continue
    op, arg = line.split(" ")
    prog.append([op, int(arg)])

print(prog)

seen = set()
ip = 0
acc = 0
while True:
    if ip in seen:
        break
    
    seen.add(ip)

    op, arg = prog[ip]

    if op == "acc":
        acc += arg
        ip += 1
    elif op == "nop":
        ip += 1
    elif op == "jmp":
        ip += arg
    else:
        raise Exception("WTF")




print(acc)
