import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import collections.abc as abc
import math
import sys
import heapq

import typing

# findall, search, parse
from parse import *
import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex
# import intervaltree as itree
# from bidict import bidict

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

positionT = tuple[int,int]
def ortho(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
    """Returns all orthagonaly adjacent points, respecting boundary conditions"""
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)

def adj(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
    """Returns all points around a point, given the shape of the array"""
    sy, sx = shape
    for dy,dx in it.product([-1,0,1], [-1,0,1]):
        if dy == 0 and dx == 0:
            continue

        py = y + dy
        px = x + dx

        if 0 <= px < sx and 0 <= py < sy:
            yield (py,px)


# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]
pos_numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))


import copy
def solve():
    mapp =  groups[0].splitlines()
    path = groups[1]
    
    # print(mapp)
    maxy = len(mapp)
    maxx = max(len(x) for x in mapp)

    board = []
    for _ in range(maxy):
        board.append([" " for _ in range(maxx)])


    for y in range(maxy):
        l = mapp[y]
        for x in range(len(l)):
            i = l[x]
            board[y][x] = i

    board2 = copy.deepcopy(board)

    for line in board:
        print("".join(line))
    
    w= """
  AB
  C
 ED
 F
    """
    GG = {"A": (0, 1), "B": (0, 2), "C": (1, 1), "D": (2, 1), "E": (2, 0), "F": (3, 0)}
    WW = {v: k for k,v in GG.items()}

    #  UP, RIGHT, DOWN, LEFT
    #  EACH ONE HAS A (Rev, NewDir)

    NEXT = {
        "A": (("FL", False, "R"), ("BL", False, "R"), ("CU", False, "D"), ("EL", True, "R")),
        "B": (("FD", False, "U"), ("DR", True, "L"), ("CR", False, "L"), ("AR", False, "L")),
        "C": (("AD", False, "U"), ("BD", False, "U"), ("DU", False, "D"), ("EU", False, "D")),
        "D": (("CD", False, "U"), ("BR", True, "L"), ("FR", False, "L"), ("ER", False, "L")),
        "E": (("CL", False, "R"), ("DL", False, "R"), ("FU", False, "D"), ("AL", True, "R")),
        "F": (("ED", False, "U"), ("DD", False, "U"), ("BU", False, "D"), ("AU", False, "D")),
    }
    # for y, line in enumerate(board):
    #     for x, char in enumerate(line):
    #         gdy, gdx = y//50, x//50
    #         if (gdy, gdx) in WW:
    #             print(WW[(gdy,gdx)], end="")
    #         else:
    #             print(" ", end="")
    #     print("")


    start_pos = (0, 0)
    for x in range(maxx):
        if board[0][x] == ".":
            start_pos = (0, x)
            break

    print(start_pos)
    
    left_rot = {"U": "L", "R": "U", "D": "R", "L": "D"}
    right_rot = {"U": "R", "R": "D", "D": "L", "L": "U"}
    delta = {"U": (-1,0), "D": (1,0), "R": (0,1), "L": (0,-1)}
    pos = start_pos
    dir = "R"
    for steps, rot in re.findall(r"([0-9]+)(R|L)?", path):
        steps = int(steps)
        # print(steps, rot)

        for _ in range(steps):
            py, px = pos
            # print(py, px)
            face =  (py//50, px//50)
            
            dy, dx = delta[dir]
            ny, nx = (py + dy), (px + dx)
            new_face = (ny//50, nx//50)
            if new_face != face:
                POS = {"U": 0, "R": 1, "D": 2, "L": 3}
                XX, REV, new_dir = NEXT[WW[face]][POS[dir]]
                NF, NS = XX[0], XX[1]
                gy, gx = GG[NF]
                gy, gx = 50*gy, 50*gx

                ly, lx = py % 50, px % 50

                dt = lx
                if dir == "R" or dir == "L":
                    dt = ly

                
                if REV:
                    dt = 49 - dt

                if NS == "U":
                    ny = gy
                    nx = gx + dt
                elif NS == "R":
                    nx = gx + 49
                    ny = gy + dt
                elif NS == "D":
                    nx = gx + dt
                    ny = gy + 49
                elif NS == "L":
                    ny = gy + dt
                    nx = gx
                else:
                    print("BIG MISTAKE")



                if board[ny][nx] == " ":
                    print(ny, nx)
                    print("THIS IS FATAL!")
                    return -1

                if board[ny][nx] == ".":
                    dir = new_dir




            if board[ny][nx] == " ":
                print("THIS IS A BIG MISTAKE")
                break


            if board[ny][nx] == "#":
                break
            else:
                pos = (ny, nx)
                board2[pos[0]][pos[1]] = {"L": "<", "U": "^", "R": ">", "D": "v"}[dir]



        if rot == "L":
            dir = left_rot[dir]
        elif rot == "R":
            dir = right_rot[dir]

        # board2[pos[0]][pos[1]] = {"L": "<", "U": "^", "R": ">", "D": "v"}[dir]
        # print("\033[H\033[J", end="")
        # for row in board2:
        #     print("".join(row))

        # input()

    
    cost = {"R": 0, "D": 1, "L": 2, "U": 3}
    print(pos, dir)
    return 1000 * (pos[0]+1) + 4*(pos[1]+1) + cost[dir]






print(solve())
