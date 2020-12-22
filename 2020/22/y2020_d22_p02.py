import fileinput as fi

import re
import itertools as it
import functools as ft

import more_itertools as mit

import math

import collections

import z3

import numpy as np

# findall
# search
# parse
from parse import *

import sys

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

INPUT = "".join(fi.input())

groups = INPUT.split("\n\n")
# print(groups[-1])
lines = list(INPUT.splitlines())

def do_nothing(*args, **kwargs): pass

debug = False
if debug:
    gprint = print
else:
    gprint = do_nothing

def zround(a, b, cache, game=1, prevgame=0, rr=1):
    assert(a)
    assert(b)
    if game != prevgame:
        gprint("=== Game {} ===".format(game))

    gprint("")
    gprint("-- Round {} (Game {}) --".format(rr, game))
    gprint("Player 1's deck: {}".format(", ".join(map(str,a))))
    gprint("Player 2's deck: {}".format(", ".join(map(str,b))))


    if (tuple(a),tuple(b)) in cache:
        gprint(" seen before!!!!!")
        return True

    cache.add((tuple(a),tuple(b)))

    # drawing top card
    aa = a.popleft()
    bb = b.popleft()
    gprint("Player 1 plays: {}".format(aa))
    gprint("Player 2 plays: {}".format(bb))

    if len(a) >= aa and len(b) >= bb:
        za = collections.deque(list(a.copy())[:aa])
        zb = collections.deque(list(b.copy())[:bb])
        gprint("Playing a sub-game to determine the winner...")
        gprint("")
        winner = zround(za, zb, set(),game=game+1,prevgame=game,rr=1)
        gprint("\n...anyway, back to game {}.".format(game))
    else:
        if aa < bb:
            winner = False
        elif bb < aa:
            winner = True

    if winner:
        gprint("Player 1 wins round {} of game {}!".format(rr, game))
        a.append(aa)
        a.append(bb)
    else:
        gprint("Player 2 wins round {} of game {}!".format(rr, game))
        b.append(bb)
        b.append(aa)
    
    # Ending game
    if len(a) == 0:
        gprint("The winner of game {} is player 2!".format(game))
        return False
    elif len(b) == 0:
        gprint("The winner of game {} is player 1!".format(game))
        return True
    
    return zround(a,b,cache,game=game,prevgame=game,rr=rr+1)

def zscore(a):
    ans = 0
    for i,x in enumerate(reversed(a),1):
        ans += i*x
    return ans


# gprint(groups)

p1d = collections.deque()
for line in groups[0].splitlines()[1:]:
    p1d.append(int(line))

p2d = collections.deque()
for line in groups[1].splitlines()[1:]:
    p2d.append(int(line))



c = set()
# while p1d and p2d:
#     gprint()
#     gprint("P1", p1d)
#     gprint("P2", p2d)
#     winner = zround(p1d, p2d, c)

winner = zround(p1d, p2d, c)

print(max([zscore(p1d), zscore(p2d)]))
# print("p1d", zscore(p1d))
# print("p2d", zscore(p2d))
