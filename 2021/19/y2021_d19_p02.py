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
from bidict import bidict

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

def get_scanners():
    scanners = []
    for group in groups:
        lines = group.splitlines()
        nr = int(lines[0].split()[-2])
        dists = [tuple(map(int,line.split(","))) for line in lines[1:]]
        scanners.append((nr, dists))

    return scanners

def get_diffs(a):
    diffs = []
    for i in range(len(a)):
        ix, iy, iz = a[i]
        daffs = []
        for j in range(len(a)):
            jx, jy, jz = a[j]
            daffs.append(math.dist(a[i], a[j]))

        diffs.append(daffs)

    return diffs
            

# check if we can get it
def check_pos(a, b):
    adiffs = get_diffs(a)
    bdiffs = get_diffs(b)

    for i in range(len(a)):
        mtch = 0
        for j in range(len(b)):
            comm = set(adiffs[i]) & set(bdiffs[j])
            if len(comm) > 11:
                return True

    
    return False

# Get the flip of b in relation to a, based on a diff
def get_flip(ad, bd):
    ax, ay, az = ad
    bx, by, bz = bd

    assert(ax != ay != az)

    trn = lambda x, y, z: (x, y, z)

    if ax == bx:
        ox = lambda p: p[0]
    elif ax == -bx:
        ox = lambda p: -p[0]
    elif ax == by:
        ox = lambda p: p[1]
    elif ax == -by:
        ox = lambda p: -p[1]
    elif ax == bz:
        ox = lambda p: p[2]
    elif ax == -bz:
        ox = lambda p: -p[2]
    else:
        raise Exception("THis is not supposed to happen")

    if ay == bx:
        oy = lambda p: p[0]
    elif ay == -bx:
        oy = lambda p: -p[0]
    elif ay == by:
        oy = lambda p: p[1]
    elif ay == -by:
        oy = lambda p: -p[1]
    elif ay == bz:
        oy = lambda p: p[2]
    elif ay == -bz:
        oy = lambda p: -p[2]
    else:
        raise Exception("THis is not supposed to happen")

    if az == bx:
        oz = lambda p: p[0]
    elif az == -bx:
        oz = lambda p: -p[0]
    elif az == by:
        oz = lambda p: p[1]
    elif az == -by:
        oz = lambda p: -p[1]
    elif az == bz:
        oz = lambda p: p[2]
    elif az == -bz:
        oz = lambda p: -p[2]
    else:
        raise Exception("THis is not supposed to happen")
    # We now must see how to flip.
    # We must map the x

    tran = lambda p: (ox(p), oy(p), oz(p))
    # print(tran((1,2,3)))
    return tran

import numpy as np
import math

def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

def do_flip(v, fl, dx, dy, dz):
    if fl:
        v = (-v[0], -v[1], -v[2])

    v = tuple(np.dot(rotation_matrix([1,0,0], dx*(math.pi/2)), v))
    v = tuple(np.dot(rotation_matrix([0,1,0], dy*(math.pi/2)), v))
    v = tuple(np.dot(rotation_matrix([0,0,1], dz*(math.pi/2)), v))
    return tuple(np.round(v).astype(int))


# for dx in range(4):
#     for dy in range(4):
#         for dz in range(4):
#             xbd = do_flip((1,0,0), False, dx, dy, dz)
#             ybd = do_flip((0,1,0), False, dx, dy, dz)
#             zbd = do_flip((0,0,1), False, dx, dy, dz)

#             g1 = xbd[0]*1 + xbd[0]*2 + xbd[0]*3
#             g2 = xbd[1]*1 + xbd[1]*2 + xbd[1]*3
#             g3 = xbd[2]*1 + xbd[2]*2 + xbd[2]*3
#             print((g1,g2,g3))
#             # print(zbd)


def get_flip2(ad, bd):
    # print(ad, bd)
    flpp = get_flip(ad, bd)
    # print(bd)
    for gbd in [False, False]:
        for dx in range(4):
            # xbd = tuple(np.dot(rotation_matrix([1,0,0], dx*(math.pi/2)), bd).astype(int))
            # if dx == 0:
            #     assert(xbd == bd)
            # print(dx, xbd)
            for dy in range(4):
                # ybd = tuple(np.dot(rotation_matrix([0,1,0], dy*(math.pi/2)), xbd).astype(int))
                for dz in range(4):
                    # zbd = tuple(np.dot(rotation_matrix([0,0,1], dz*(math.pi/2)), ybd).astype(int))
                    zbd = do_flip(bd, gbd, dx, dy, dz)
                    # print(ad, zbd)
                    if zbd == ad:
                        # print("wow", dx, dy, dz)
                        # mmat = (rotation_matrix([1,0,0], dx*(math.pi/2)) @ 
                        # rotation_matrix([0,1,0], dy*(math.pi/2)) ) @ rotation_matrix([0,0,1], dz*(math.pi/2))
                        # tbd = tuple(np.dot(mmat, bd).astype(int))
                        # print(zbd)
                        # assert(tbd == zbd)
                        tran =  lambda p: do_flip(p, gbd, dx, dy, dz)
                        assert(tran(bd) == flpp(bd))
                        return flpp
    
    print("No match found: {} {}".format(ad, bd))
    return None

                
    

# Orient b in relation to a, return a flip and a relative rotation
def orient(a, b):
    adiffs = get_diffs(a)
    bdiffs = get_diffs(b)

    omatch = bidict()
    for i in range(len(a)):
        mtch = 0
        for j in range(len(b)):
            match = bidict()
            for ii, di in enumerate(adiffs[i]):
                for jj, dj in enumerate(bdiffs[j]):
                    if di == dj and di != 0:
                        if ii in match:
                            # print("hhmm")
                            pass
                        else:
                            match[ii] = jj

            if len(match) > 10:
                print("J", match)
                for ii, jj in match.items():
                    a1 = a[i]
                    a2 = a[ii]
                    b1 = b[j]
                    b2 = b[jj]
                    ad = tuple(x-y for x,y in zip(a1,a2))
                    bd = tuple(x-y for x,y in zip(b1,b2))

                    # print(i, jj)
                    # print(ad, bd)
                    flap = get_flip2(ad, bd)
                    # if flap is None:
                    #     return None, None
                    corr_b = flap(b1)
                    offset_b = tuple(x - y for y,x in zip(corr_b, a1))
                    return (flap, offset_b)

    return None, None
    # print(omatch)
    

def solve2():
    scanners = get_scanners()

    # We say that Q is correct.
    known_pos = {0: (0,0,0)}
    seen = set()
    Q = set([0])
    while len(Q) > 0:
        print("KN", known_pos)
        ai = Q.pop()
        if ai in seen:
            continue
        else:
            seen.add(ai)

        axs = scanners[ai][1]

        gprint("=== We are looking for beacons near {} ===".format(ai))

        for bi, bxs in scanners:
            if bi in seen:
                continue

            gprint("Considering beacon {}".format(bi))
            if check_pos(axs, bxs):
                gprint("We might have a hit")
                b_flap, b_offset = orient(axs, bxs)
                dx, dy, dz = b_offset
                print(b_flap((1,2,3)))
                print(b_offset)

                known_pos[bi] = b_offset
                roted = list(b_flap(p) for p in bxs)
                rated = [(x + dx, y + dy, z + dz) for x,y,z in roted]
                scanners[bi] = (bi, rated)
                Q.add(bi)


    sat = set()
    for _, ps in scanners:
        sat.update(ps)

    # print(sat)
    # return len(sat)

    print()
    ans = max(abs(ax-bx) + abs(ay-by) + abs(az-bz) for ((ax,ay,az), (bx,by,bz)) in it.combinations(known_pos.values(), 2))
    return ans
                



        
    



def solve():
    matches = cs.defaultdict(set)
    for (an, ax), (bn, bx) in it.combinations(scanners, r=2):
        if check_pos(ax, bx):
            matches[an].add(bn)
            matches[bn].add(an)

    print(matches)
    id_flap = lambda p: p
    offset_f = lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2])

    known_pos = {0: (0,0,0)}
    known_flap = {0: id_flap}

    Q = set([0])
    while len(Q) > 0:
        ai = Q.pop()

        a_flap = known_flap[ai]
        a_offset = known_pos[ai]
        a_corr = [offset_f(a_offset, a_flap(p)) for p in scanners[ai][1]]
        # print(a_corr)

        for bi in matches[ai]:
            # print("KN: ", known_pos)
            if bi in known_pos:
                continue

            # print(ai, bi)
            # b_flap, b_offset = orient(a_corr, scanners[bi][1])
            b_flap, b_offset = orient(scanners[ai][1], scanners[bi][1])
            if b_flap is None:
                print("We had a wrong match!")
                continue

            known_pos[bi] = (b_offset[0] + a_offset[0],b_offset[1] + a_offset[1],b_offset[2] + a_offset[2])
            known_pos[bi] = b_offset
            # tr = lambda p: a_flap(b_flap(p))
            known_flap[bi] = tr # b_flap

            Q.add(bi)

    print(known_pos)


print(solve2())
# print(solve())
