import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys
import heapq

# findall, search, parse
# from parse import *
import more_itertools as mit
# import z3
import numpy as np
# import lark
# import regex
# import intervaltree as itree

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())

def step(par):
    p, v, a = par
    px, py, pz = p
    vx, vy, vz = v
    ax, ay, az = a
    
    vx += ax
    vy += ay
    vz += az

    px += vx
    py += vy
    pz += vz

    return ((px, py, pz), (vx, vy, vz), (ax, ay, az))

def dist(par):
    return abs(par[0][0]) + abs(par[0][1]) + abs(par[0][2])


    

pars = []
for line in lines:
    p, v, a = line.split(", ")
    px, py, pz = map(int, p[3:-1].split(","))
    vx, vy, vz = map(int, v[3:-1].split(","))
    ax, ay, az = map(int, a[3:-1].split(","))
    p = (px, py, pz)
    v = (vx, vy, vz)
    a = (ax, ay, az)
    par = (p ,v, a)

    pv = lambda t: np.array([px, py, pz])
    pars.append(par)


import sympy
def sympy_can_colide(a, b):
    ap, av, aa = a
    bp, bv, ba = b

    t = sympy.symbols('t', integer=True)

    a_exs = [p + v*t + (a*t*(t+1))/2 for (p, v, a) in zip(ap, av, aa)]
    b_exs = [p + v*t + (a*t*(t+1))/2 for (p, v, a) in zip(bp, bv, ba)]
    # exs = [sympy.Eq(ax, bx) for ax, bx in zip(a_exs, b_exs)]
    # print(sympy.solveset(exs, t, domain=sympy.S.Integers))

    doms = []
    dom = sympy.Integers
    for ax, bx in zip(a_exs, b_exs):
        w = sympy.Eq(ax, bx)
        sl = sympy.solveset(w, t, domain=sympy.S.Integers)
        dom = dom.intersect(sl)

        if dom == sympy.EmptySet:
            return None


    if dom != sympy.EmptySet:
        # print(a)
        # print(b)
        # print(dom)
        return dom

    return None

import math
def my_can_collide(a, b):
    # ap, av, aa = a
    # bp, bv, ba = b
    
    ans = None
    for (ap, av, aa), (bp, bv, ba) in zip(zip(*a), zip(*b)):
        kc = ap - bp
        kb = av - bv
        ka = aa - ba

        if ka == 0:
            # print("Kicking the ball to sympy")
            return sympy_can_colide(a, b)


        # print(kb)
        # print(ka)
        if (kb*kb - 4*ka*kc) < 0:
            return None

        x1 = (-kb + math.sqrt(kb*kb - 4*ka*kc)) / 2*ka
        dw1 = math.remainder((-kb + math.sqrt(kb*kb - 4*ka*kc)) , 2*ka)
        x2 = (-kb - math.sqrt(kb*kb - 4*ka*kc)) / 2*ka
        dw2 = math.remainder((-kb - math.sqrt(kb*kb - 4*ka*kc)) , 2*ka)

        if abs(dw1) < 0.00001:
            if ans is None:
                ans = int(x1)

            if ans != int(x1):
                return None

            # print("YE")
            # print(x1)
            # print(dw1)
        elif abs(dw2) < 0.00001:
            if ans is None:
                ans = int(x1)

            if ans != int(x1):
                return None
        else:
            return None

        # print(x1, dw1)
        # print(x2, dw2)

        # print("HERE")

    
    return ans

def can_collide(a, b):
    # mc =  my_can_collide(a, b)
    sc = sympy_can_colide(a, b)

    # assert(mc == sc)

    return sc

def clean(pars):
    seen = {}
    to_remove = set()
    for i, par in enumerate(pars):
        p, v, a = par
        if p in seen:
            to_remove.add(i)
            to_remove.add(seen[p])
        else:
            seen[p] = i

    for x in reversed(sorted(to_remove)):
        print("Removing {}, ({})".format(x, pars[x]))
        del pars[x]

    return pars

import tqdm        
import copy
def brute(pars):
    pars = clean(pars)

    for i in tqdm.trange(10000):
        pars = [step(par) for par in pars]
        ll = len(pars)
        pars = clean(pars)
        ww = len(pars)
        dd = ll - ww
        
        if dd > 0:
            print("At {} we removed {}. We now have {}".format(i, dd, ww))

    return pars


def binomial_cooefficient(n: int, k: int) -> int:
    n_fac = math.factorial(n)
    k_fac = math.factorial(k)
    n_minus_k_fac = math.factorial(n - k)
    return n_fac/(k_fac*n_minus_k_fac)


# print(pars[279])
# print(pars[280])
pars = brute(pars)
# print(can_collide(pars[280], pars[279]))

# a = pars[279]
# b = pars[280]



tq = tqdm.tqdm(it.combinations(enumerate(pars), 2), total=binomial_cooefficient(len(pars), 2))
prev_thing = 0
collided = False
for (i, a), (j, b) in tq:
    if (i != prev_thing):
        if not collided:
            tq.write("{} did not collide with anything".format(prev_thing))
        else:
            tq.write("{} did collide with somethign".format(prev_thing))

        collided = False
        prev_thing = i
    
    t = can_collide(a, b)
    if t:
        # print("{} can colide with {} at {}, ({}, {})".format(i, j, t, a, b))
        tq.write("{} can colide with {} at {}, ({}, {})".format(i, j, t, a, b))
        collided = True
    # else:
        # print("{} can't colide with {}, ({}, {})".format(i, j,  a, b))
        # tq.write("{} can't colide with {}, ({}, {})".format(i, j,  a, b))



