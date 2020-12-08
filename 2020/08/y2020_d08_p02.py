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


def does_terminate(prog):
    seen = set()
    ip = 0
    acc = 0
    while True:
        if ip in seen:
            return None
        
        if ip == len(prog):
            return acc
        
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

for i in range(len(prog)):
    op, arg = prog[i]
    if op == "acc":
        continue

    # try to flip it
    if op  == "jmp":
        new_op, old_op = "nop", "jmp"
    else:
        new_op, old_op = "jmp", "nop"
    
    prog[i][0] = new_op
    ans = does_terminate(prog)
    if ans:
        print(ans)
    
    prog[i][0] = old_op








# print(acc)
