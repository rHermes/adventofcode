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

def collide(a, b):
    (min_x1,max_x1), (min_y1,max_y1), (min_z1, max_z1) = a
    (min_x2,max_x2), (min_y2,max_y2), (min_z2, max_z2) = b
    if max_x1 < min_x2:
        return False
    if (min_y1 > max_y2):
        return False
    if (max_y1 < min_y2):
        return False
    if (min_z1 > max_z2):
        return False
    if (max_z1 < min_z2):
        return False

    return True


# Returns (a - b, a & b, b - a)
def overlap_region(a,b):
    (min_x1,max_x1), (min_y1,max_y1), (min_z1, max_z1) = a
    (min_x2,max_x2), (min_y2,max_y2), (min_z2, max_z2) = b

    if not collide(a,b):
        return (a, None, b)

    # The overlap must either be partial or not.
    if min_x1 < min_x2:
        pass





def volume(a):
    (min_x1,max_x1), (min_y1,max_y1), (min_z1, max_z1) = a
    return (max_x1-min_x1)*(max_y1-min_y1)*(max_z1 - min_z1)


# Returns a new list of cubes, that don't touch the a
def cremove(a, b):
    if not collide(a,b):
        return [b]



    raise Exception("NOOO")


from intervaltree import IntervalTree, Interval

from copy import deepcopy

def fff(iv, thing):
    return deepcopy(iv.data)

def remove_from(tree, a):
    xmin,xmax,ymin,ymax,zmin,zmax = a

    # print("removing", a)
    tree.slice(xmin, datafunc=fff)
    tree.slice(xmax+1, datafunc=fff)
    for xis in tree[xmin:xmax+1]:
        xis.data.slice(ymin, datafunc=fff)
        xis.data.slice(ymax+1, datafunc=fff)
        for yis in xis.data[ymin:ymax+1]:
            # print((zmin,zmax))
            # print(sorted(yis.data))
            yis.data.slice(zmin, datafunc=fff)
            yis.data.slice(zmax+1, datafunc=fff)
            # print(sorted(yis.data))

            ggg = yis.data[zmin:zmax+1]
            gga = yis.data.envelop(zmin, zmax+1)

            if len(ggg) != len(gga):
                print("WTF")
                print(sorted(ggg))
                print(sorted(gga))
                assert(False)

            yis.data.remove_envelop(zmin, zmax+1)


def add_to(tree, a):
    xmin,xmax,ymin,ymax,zmin,zmax = a
    remove_from(tree, a)


    # Now add our tree
    zt = IntervalTree()
    zt.addi(zmin,zmax+1)
    yt = IntervalTree()
    yt.addi(ymin,ymax+1,data=zt)
    tree.addi(xmin,xmax+1,data=yt)
    # Now we are in the 



def gol(tree):
    ans = 0
    # print(tree)
    for xi in tree:
        dx = xi.end - xi.begin
        for yi in xi.data:
            dy = yi.end - yi.begin
            for zi in yi.data:
                dz = zi.end - zi.begin
                ans += dx*dy*dz

    return ans


def solve():
    tree = IntervalTree()
    for i, line in enumerate(lines):
        print("{} of {}: {}".format(i, len(lines), line))
        to, xmin,xmax,ymin,ymax,zmin,zmax = parse("{} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}", line)
        w = to == "on"

        if to == "on":
            add_to(tree,(xmin,xmax,ymin,ymax,zmin,zmax))
        else:
            remove_from(tree,(xmin,xmax,ymin,ymax,zmin,zmax))





    return gol(tree)
       

print(solve())
