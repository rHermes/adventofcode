import fileinput as fi

import copy
import re
import itertools as it
import functools as ft

import more_itertools as mit

import math

import collections

import z3

import numpy as np

import string

# findall
# search
# parse
from parse import *

INPUT = "".join(fi.input()).rstrip()

groups = INPUT.split("\n\n")
# print(groups[-1])
lines = list(INPUT.splitlines())

def print_board(board):
    Y = len(board)-2
    X = len(board[0]) - 2
    for y in range(1,Y+1):
        for x in range(1, X+1):
            if board[y][x]:
                print("#", end="")
            else:
                print(".", end="")
        print("")

board = []
for line in lines:
    board.append([False] + [c == "#" for c in line] + [False])

board = [[False for _ in board[0]]] + board + [[False for _ in board[0]]]


def step(board):
    Y = len(board)-2
    X = len(board[0]) - 2

    nboard = copy.deepcopy(board)

    for y in range(1,Y+1):
        for x in range(1,X+1):
            neights = [
                board[y-1][x-1],
                board[y-1][x],
                board[y-1][x+1],
                board[y][x-1],
                board[y][x+1],
                board[y+1][x-1],
                board[y+1][x],
                board[y+1][x+1],
            ]
            non = sum(neights)

            if board[y][x]:
                if not (non == 2 or non == 3):
                    nboard[y][x] = False
            else:
                if non == 3:
                    nboard[y][x] = True

    nboard[1][1] = True
    nboard[1][X] = True
    nboard[Y][1] = True
    nboard[Y][X] = True
    return nboard

nboard = board
for gen in range(100):
    nboard = step(nboard)

print(sum(sum(x) for x in nboard))

