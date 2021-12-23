import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import math
import sys
import heapq

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

def ortho(y, x, shape):
    """Returns all orthagonaly adjacent points, respecting boundary conditions"""
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)

def adj(y, x, shape):
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
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))

DESIRED_COL = {"A": 3, "B": 5, "C": 7, "D": 9}
DESIRED = {"A": {(2,3), (3,3), (4,3), (5,3)}, "B": {(2,5),(3,5),(4,5),(5,5)}, "C": {(2,7), (3,7), (4,7), (5,7)}, "D": {(2,9),(3,9),(4,9),(5,9)}}
COST = {"A": 1, "B": 10, "C": 100, "D": 1000}

def parse_input():
    pods = {}
    grid = cs.defaultdict(bool)
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c in ".ABCD":
                grid[(y,x)] = True

            if c in "ABCD":
                if c+"3" in pods:
                    pods[c+"4"] = (y,x)
                elif c+"2" in pods:
                    pods[c+"3"] = (y,x)
                elif c+"1" in pods:
                    pods[c+"2"] = (y,x)
                else:
                    pods[c+"1"] = (y,x)
    
    return pods, grid

def is_done(pods):
    for k, v in DESIRED.items():
        if {pods[k+"1"], pods[k+"2"], pods[k+"3"], pods[k+"4"]} != v:
            break
    else:
        return True

    return False

def get_pods_moves(pods, grid):
    taken = set(pods.values())
    gmo = {}
    for pod, src in pods.items():
        costs = {}
        # We skip all if we have what we need
        if {pods[pod[0]+x] for x in "1234"} == DESIRED[pod[0]]:
            gmo[pod] = costs
            continue

        Q = [(0, src)]
        while Q:
            cost, pos = heapq.heappop(Q)
            if pos in costs:
                continue
            else:
                costs[pos] = cost

            for ty, tx in ortho(pos[0], pos[1], (10000,10000)):
                if (ty,tx) not in taken and grid[(ty,tx)]:
                    heapq.heappush(Q,(cost+COST[pod[0]], (ty,tx)))

        # Now a filter pass
        
        # Delete itself
        del costs[src]

        # Remove any of the spots outside the rooms
        for x in [3,5,7,9]:
            if (1,x) in costs:
                del costs[(1,x)]

            if DESIRED_COL[pod[0]] != x:
                for p in [(2,x), (3,x)]:
                    if p in costs:
                        del costs[p]
            else:
                p1 = (2,x)
                p2 = (3,x)
                found = False
                for dy,dx in DESIRED[pod[0]]:
                    for kk, vv in pods.items():
                        if kk[0] == pod[0]:
                            continue

                        if (dy,dx) == vv:
                            break
                    else:
                        continue

                    found = True
                    break

                if found:
                    # print("Can't move to this room")
                    for p in DESIRED[pod[0]]:
                        if p in costs:
                            del costs[p]

                    
        # If we are in a hallway, we delete all but our desired spots
        if src[0] == 1:
            pwd = list(costs.keys())
            for y,x in pwd:
                if (y,x) not in DESIRED[pod[0]]:
                    del costs[(y,x)]
        

        gmo[pod] = costs

    return gmo



def to_tup(pods):
    # I think we can just sort them
    gav = {"A": set(), "B": set(), "C": set(), "D": set()}
    for pod, place in pods.items():
        gav[pod[0]].add(place)

    return tuple(sorted((k, frozenset(b)) for k, b in gav.items()))
    # return tuple(sorted(pods.items()))

def from_tup(t):
    pods = {}
    for k, v in t:
        for place, nn in zip(v, "1234"):
            pods[k+nn] = place

    return pods


# Heruistic of how far we are away. This must be atleast the manhatan distance times the cost
def heru(pods):
    ans = 0
    for pod, place in pods.items():
        py, px = place
        desired_col = DESIRED_COL[pod[0]]
        if px == desired_col:
            continue

        steps = (py-1) # Move up
        steps += abs(desired_col-px) # Move to the column
        steps += 1 # Move down to the first step

        ans += COST[pod[0]]*steps

    # There is also the question of shuffeling internally.
    # If 4 pods are out of place, then 1 goes from 
    # for pn in "ABCD":
    #     kv = 4 - len({pods[pn+x] for x in "1234"} & DESIRED[pn])
    #     steps = 0
    #     if 3 < kv:
    #         steps += 3
    #     if 2 < kv:
    #         steps += 2
    #     if 1 < kv:
    #         steps += 1

    #     ans += COST[pn]*steps

    return ans


def solve():
    pods, grid = parse_input()

    Q = [(0, 0 + heru(pods), 0, to_tup(pods))]
    print(Q)

    # high_cost 
    high_cost = 0
    low_heru = 100000000000000000000000
    high_moves = 0
    # pbar = tqdm()
    seen = set()
    while len(Q) > 0:
        moves, harhar, cost, pods = heapq.heappop(Q)
        if pods in seen:
            continue
        else:
            seen.add(pods)

        # harhar -= cost
        

        if harhar < low_heru:
            low_heru = harhar
            print("We have new low heru with: {}, {}".format(low_heru, pods))

        if moves < high_moves:
            high_moves = moves
            print("We have new high moves with: {} {}".format(high_moves, pods))


        if high_cost < cost:
            high_cost = cost
            print("We have new high cost with: {} {} {}".format(high_cost, moves, pods))

        # print(cost, pods)

        pods = from_tup(pods)

        if is_done(pods):
            return cost

        gmo = get_pods_moves(pods, grid)
        # print(gmo)
        for pod, costs in gmo.items():
            for place, mcost in costs.items():
                npods = pods.copy()
                npods[pod] = place

                # DFS
                # inst += 1
                heapq.heappush(Q, (moves + 0, heru(npods) + cost + mcost, cost + mcost,to_tup(npods)))
                # heapq.heappush(Q, (moves + 0, heru(npods), cost + mcost,to_tup(npods)))

print(solve())
