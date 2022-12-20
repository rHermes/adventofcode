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
import tqdm

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

# (y,x)
shapes = [
        ((0, 0), (0,1), (0, 2), (0,3)),
        ((0, 1), (1,0), (1,1), (1,2), (2,1)),
        ((0, 0), (0, 1), (0, 2), (1,2), (2,2)),
        ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((0, 0), (0, 1), (1, 0), (1, 1)),
]

LIMIT = 1000000000000

def hits(world, shape, curfloor=0):
    for (y,x) in shape:
        if x == -1 or x == 7 or y == curfloor or (y,x) in world:
            return True

    return False

# floorlevel, rocks_dropped, seq_index, world
worldstate_type = tuple[int, int, int, frozenset[tuple[int,int]]]

# rocks_idx, seq_index, fworld
cache_key = tuple[int, int, frozenset[tuple[int,int]]]
# delta_height, delta_rocks, seq_index, fworld
cache_value = tuple[int, int, int, frozenset[tuple[int,int]]]

def get_cache_key(sequence: str, state: worldstate_type) -> cache_key:
    floor_level, rocks_dropped, seq_index, fworld = state
    kkey: cache_key = (rocks_dropped % len(shapes), seq_index, fworld)
    return kkey


cache: dict[cache_key, cache_value] = {}
def until_clean_or_stop(sequence: str, state: worldstate_type) -> worldstate_type:
    floor_level, rocks_dropped, seq_index, fworld = state
    ofloor_level, orocks_dropped , _, _ = state

    kkey: cache_key = get_cache_key(sequence, state)
    sig = kkey
    fucked_up = False
    if sig in cache:
        delta_height, delta_rocks, sseq_index, sfworld = cache[sig]
        if rocks_dropped + delta_rocks < LIMIT:
            return (floor_level + delta_height, rocks_dropped + delta_rocks, sseq_index, sfworld)
        else:
            # fucked_up = True
            print("we at the end so we need to calculate")
        


    world = set(fworld)

    tallest = max((y for y, _ in world), default=0)
    
    # print(rocks_dropped)
    # We store everything relative to the current floor
    while rocks_dropped < LIMIT:
        if fucked_up:
            # print(rocks_dropped)
            pass
        shapeIndex = rocks_dropped % len(shapes)

        shp = shapes[shapeIndex]
        rocks_dropped += 1



        relpos = (tallest+4, 2)
        shp = tuple((y+relpos[0], x+relpos[1]) for y,x in shp)

        while True:
            s = sequence[seq_index]
            seq_index = (seq_index + 1) % len(sequence)
            if s == '>':
                delta = (0, 1)
            else:
                delta = (0, -1)
                
            pos_new = tuple((y+delta[0], x+delta[1]) for y,x in shp)
            if not hits(world, pos_new):
                shp = pos_new

            # Move down
            pos_new = tuple((y-1, x) for y,x in shp)
            if hits(world, pos_new):
                world.update(shp)
                tallest = max(tallest, max(y for y,_ in shp))
                break
            else:
                shp = pos_new

        lowest = None
        for i in reversed(range(max(tallest - 200, -1), tallest+1)):
            if all((i, x) in world for x in range(0, 7)):
                # print("We have a full down at {}".format(i))
                lowest = i
                break

        # if num_rock % 10000 == 0:
        #     print(len(world))

        if lowest:
            # print("We are cleaning anything below: ")
            toclean = set()
            for y,x in world:
                if y < lowest :
                    # print("cleaning up")
                    toclean.add((y,x))
            
            if toclean:
                # print("We are cleaning up: {} entries".format(len(toclean)))
                world -= toclean

            break
    
    # We now get the floor
    newFloor = min(y for y, _ in world)
    newWorld = frozenset((y-newFloor, x) for y,x in world if y != newFloor)

    # floorlevel, rocks_dropped, seq_index, world
    ans = (newFloor+ofloor_level, rocks_dropped, seq_index, newWorld)
    # delta_height, delta_rocks, seq_index, fworld
    # if sig not in cache:
    if True:
        cvalve = (newFloor, rocks_dropped - orocks_dropped, seq_index, newWorld)
        cache[sig] = cvalve
    return ans

    

import tqdm
def solve():
    global cache
    sequence = lines[0]
    state: worldstate_type = (0, 0, 0, frozenset())

    with tqdm.tqdm(total=LIMIT, miniters=1) as pbar:
        while True:
            new_state = until_clean_or_stop(sequence, state)

            # print("we went from {} to {}".format(state, new_state))
            pbar.update(new_state[1] - state[1])
            # print(new_state[1] - state[1])
            state = new_state

            # print(state[1] / LIMIT)
            kkey = get_cache_key(sequence, new_state)
            if kkey in cache:
                break

            if LIMIT < state[1]:
                print("BIG MISTAKE HERE")
                break
            elif LIMIT == state[1]:
                print("WE DONE")
                break

        # We now have a complete graph
        print("We have a complete graph")
        start = get_cache_key(sequence, state)
        floor_delta = 0
        rocks_delta = 0
        while True:
            new_state = until_clean_or_stop(sequence, state)
            floor_delta += new_state[0] - state[0]
            rocks_delta += new_state[1] - state[1]
            pbar.update(new_state[1] - state[1])
            state = new_state


            if get_cache_key(sequence, state) == start:
                break
        
        # Iterate quickly trough it
        # print(floor_delta, rocks_delta)
        times = (LIMIT - state[1]) // rocks_delta
        tot_rock_delta = times * rocks_delta
        tot_floor_delta = times * floor_delta
        pbar.update(tot_rock_delta)
        state = (state[0] + tot_floor_delta, state[1] + tot_rock_delta, state[2], state[3])

        while True:
            new_state = until_clean_or_stop(sequence, state)

            # print("we went from {} to {}".format(state, new_state))
            pbar.update(new_state[1] - state[1])
            # print(new_state[1] - state[1])
            state = new_state

            # # print(state[1] / LIMIT)
            # kkey = get_cache_key(sequence, new_state)
            # if kkey in cache:
            #     break

            if LIMIT < state[1]:
                print("BIG MISTAKE HERE")
                break
            elif LIMIT == state[1]:
                print("WE DONE")
                break

    
    tallest = max((y for y, _ in state[3]), default=0)
    print(tallest + state[0])
    print(state)
    return tallest + state[0]


print(solve())



def solve2():
    sequence = list(lines[0])

    # sequence = it.cycle(enumerate(lines[0]))

    world = set()
    tallest = 0
    for (shp_idx, shp), num_rock in zip(it.cycle(enumerate(shapes)), tqdm.trange(1000000000000)):
        lowest = None
        for i in reversed(range(tallest - 20, tallest+1)):
            if all((i, x) in world for x in range(0, 7)):
                # print("We have a full down at {}".format(i))
                lowest = i
                break

        if lowest and tallest == lowest:
            print("HALELJUA")

        # if num_rock % 10000 == 0:
        #     print(len(world))

        if lowest:
            # print("We are cleaning anything below: ")
            toclean = set()
            for y,x in world:
                if y < lowest :
                    # print("cleaning up")
                    toclean.add((y,x))
            
            if toclean:
                print("We are cleaning up: {} entries".format(len(toclean)))
                world -= toclean


        relpos = (tallest+4, 2)
        shp = tuple((y+relpos[0], x+relpos[1]) for y,x in shp)
        
        first = True
        for (ix, s) in sequence:
            if ix == 0 and shp_idx == 0 and first:
                print(num_rock-1, tallest)

            first = False
            if s == '>':
                delta = (0, 1)
            else:
                delta = (0, -1)
                
            pos_new = tuple((y+delta[0], x+delta[1]) for y,x in shp)
            if not hits(world, pos_new):
                shp = pos_new

            # Move down
            pos_new = tuple((y-1, x) for y,x in shp)
            if hits(world, pos_new):
                world.update(shp)
                tallest = max(tallest, max(y for y,_ in shp))
                break
            else:
                shp = pos_new

    return tallest

