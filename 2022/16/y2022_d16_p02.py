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
# import more_itertools as mit
# # import z3
# # import numpy as np
# # import lark
# # import regex
# # import intervaltree as itree
# from bidict import bidict

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
# def gprint(*args, **kwargs):
#     if DEBUG: print(*args, **kwargs)

# positionT = tuple[int,int]
# def ortho(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
#     """Returns all orthagonaly adjacent points, respecting boundary conditions"""
#     sy, sx = shape
#     if 0 < x: yield (y, x-1)
#     if x < sx-1: yield (y, x+1)
#     if 0 < y: yield (y-1, x)
#     if y < sy-1: yield (y+1, x)

# def adj(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
#     """Returns all points around a point, given the shape of the array"""
#     sy, sx = shape
#     for dy,dx in it.product([-1,0,1], [-1,0,1]):
#         if dy == 0 and dx == 0:
#             continue

#         py = y + dy
#         px = x + dx

#         if 0 <= px < sx and 0 <= py < sy:
#             yield (py,px)


# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]
pos_numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))

cache = {}
max_rem = 0
def best(valves, dists, iremaining, eremaining, notdone: frozenset[str], inode: str, enode: str):
    global cache
    if (iremaining == 0 and eremaining == 0) or len(notdone) == 0:
        return 0
    
    if enode < inode:
        iremaining, eremaining = eremaining, iremaining
        inode, enode = enode, inode

    if (iremaining, eremaining, notdone, inode, enode) in cache:
        return cache[(iremaining, eremaining, notdone, inode, enode)]

    ##
    #erate, ecango = valves[enode]
    #irate, icango = valves[inode]


    ans = 0
    for ennode in notdone:
        cost = dists[(enode, ennode)]
        time_left_then = eremaining - cost -1
        if time_left_then < 1:
            continue


        ennode_rate, _ = valves[ennode]
        nwdone = notdone - frozenset([ennode])
        sw = time_left_then * ennode_rate
        ans = max(ans, sw + best(valves, dists, iremaining, time_left_then, nwdone, inode, ennode))

    for innode in notdone:
        cost = dists[(inode, innode)]
        time_left_then = iremaining - cost -1
        if time_left_then < 1:
            continue


        innode_rate, _ = valves[innode]
        nwdone = notdone - frozenset([innode])
        sw = time_left_then * innode_rate
        ans = max(ans, sw + best(valves, dists, time_left_then, eremaining, nwdone, innode, enode))


    # global max_rem 
    # if max_rem < remaining:
    #     print(remaining, open, inode, enode, ans)
    #     max_rem = remaining

    cache[(iremaining, eremaining, notdone, inode, enode)] = ans
    return ans









def solve():
    valves = {}
    for line in lines:
        name, rate, _, _, _, leads = parse("Valve {} has flow rate={:d}; {} {} to {} {}", line)
        leads = leads.split(", ")
        valves[name] = (rate, leads)

    # We build a fast way to see
    dists = cs.defaultdict(lambda: 10000000000000)
    for src, (_, dsts) in valves.items():
        dists[(src,src)] = 0
        for dst in dsts:
            dists[(src,dst)] = 1
    
    ks = list(valves.keys())
    for k in ks:
        for i in ks:
            for j in ks:
                if dists[(i,j)] > dists[(i,k)] + dists[(k,j)]:
                    dists[(i,j)] = dists[(i,k)] + dists[(k,j)]

    # print(dists)


        

    # prod_valves = {'QJ': (11, ['HB', 'GL']), 'VZ': (10, ['NE']), 'TX': (19, ['MG', 'OQ', 'HM']), 'ZI': (5, ['BY', 'ON', 'RU', 'LF', 'JR']), 'IH': (0, ['YB', 'QS']), 'QS': (22, ['IH']), 'QB': (0, ['QX', 'ES']), 'NX': (0, ['UH', 'OP']), 'PJ': (0, ['OC', 'UH']), 'OR': (6, ['QH', 'BH', 'HB', 'JD']), 'OC': (7, ['IZ', 'JR', 'TA', 'ZH', 'PJ']), 'UC': (0, ['AA', 'BY']), 'QX': (0, ['AA', 'QB']), 'IZ': (0, ['OC', 'SX']), 'AG': (13, ['NW', 'GL', 'SM']), 'ON': (0, ['MO', 'ZI']), 'XT': (18, ['QZ', 'PG']), 'AX': (0, ['UH', 'MO']), 'JD': (0, ['OR', 'SM']), 'HM': (0, ['TX', 'QH']), 'LF': (0, ['ZI', 'UH']), 'QH': (0, ['OR', 'HM']), 'RT': (21, ['PG']), 'NE': (0, ['VZ', 'TA']), 'OQ': (0, ['TX', 'GE']), 'AA': (0, ['QZ', 'UC', 'OP', 'QX', 'EH']), 'UH': (17, ['PJ', 'NX', 'AX', 'LF']), 'GE': (0, ['YB', 'OQ']), 'EH': (0, ['AA', 'MO']), 'MG': (0, ['TX', 'NW']), 'YB': (20, ['IH', 'GE', 'XG']), 'MO': (15, ['EH', 'ON', 'AX', 'ZH', 'CB']), 'JR': (0, ['ZI', 'OC']), 'GL': (0, ['AG', 'QJ']), 'SM': (0, ['JD', 'AG']), 'HB': (0, ['OR', 'QJ']), 'TA': (0, ['OC', 'NE']), 'PG': (0, ['RT', 'XT']), 'XG': (0, ['CB', 'YB']), 'ES': (9, ['QB', 'FL']), 'BH': (0, ['RU', 'OR']), 'FL': (0, ['SX', 'ES']), 'CB': (0, ['MO', 'XG']), 'QZ': (0, ['AA', 'XT']), 'BY': (0, ['UC', 'ZI']), 'ZH': (0, ['MO', 'OC']), 'OP': (0, ['NX', 'AA']), 'NW': (0, ['MG', 'AG']), 'RU': (0, ['ZI', 'BH']), 'SX': (16, ['IZ', 'FL'])}

    # print(valves)

    notdone = frozenset(sorted(a for a, (rate,_) in valves.items() if rate != 0))
    print(notdone)

    return best(valves, dists, 26, 26, notdone, "AA", "AA")



print(solve())
