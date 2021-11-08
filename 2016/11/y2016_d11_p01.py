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
# import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex

import copy

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

# Input parsing
# INPUT = "".join(fi.input()).rstrip()
# groups = INPUT.split("\n\n")
# lines = list(INPUT.splitlines())

Generator = collections.namedtuple("Generator", ["t", "k"])
Chip = collections.namedtuple("Chip", ["t", "k"])


class Floor():
    def __init__(self, generators, chips):
        # self.gens = tuple(sorted(generators))
        # self.chips = tuple(sorted(chips))
        self.gens = generators
        self.chips = chips

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.gens == other.gens and self.chips == other.chips

    def __repr__(self):
        return "Floor: {} {}".format(["G({})".format(x.t) for x in self.gens], ["C({})".format(x.t) for x in self.chips])

    def __hash__(self):
        return hash((self.gens, self.chips))

    def valid(self):
        if len(self.gens) == 0:
            return True
        if len(self.chips) == 0:
            return True

        for chip in self.chips:
            for gens in self.gens:
                if chip.t == gens.t:
                    break
            else:
                return False
        
        return True



class Elevator():
    def __init__(self, floor, generators, chips):
        self.floor = floor
        # self.gens = tuple(sorted(generators))
        # self.chips = tuple(sorted(chips))
        self.gens = generators
        self.chips = chips

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.floor == other.floor and self.gens == other.gens and self.chips == other.chips

    def __hash__(self):
        return hash((self.floor, self.gens, self.chips))

    def __repr__(self):
        return "Elevator: {} {} {}".format(repr(self.floor), repr(self.gens), repr(self.chips))


    def valid(self, floor):
        return 0 <= self.floor < 4 and Floor(self.gens + floor.gens, self.chips + floor.chips).valid()



class State():
    def __init__(self, floor1, floor2, floor3, floor4, elevator):
        self.floors = (floor1, floor2, floor3, floor4)
        self.e = elevator

        self.sig = self.signature()

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        if self.e.floor != other.e.floor:
            return False

        # ansA = self.signature == other.signature
        ansA = self.sig == other.sig
        # ansB = (self.floors == other.floors and self.e == other.e)
        # if ansA != ansB:
        #     # print("We skipped a state {} vs {}".format(ansA, ansB))
        #     return ansA

        return ansA

        # return self.floors == other.floors and self.e == other.e
    
    # @property
    # @ft.cached_property
    def signature(self):
        gens = {}
        chips = {}
        for i, floor in enumerate(self.floors):
            for x in floor.gens:
                gens[x.t] = i

            for x in floor.chips:
                chips[x.t] = i

        for x in self.e.gens:
            gens[x.t] = self.e.floor

        for x in self.e.chips:
            chips[x.t] = self.e.floor

        # print(gens)
        # print(chips)

        sig = tuple(sorted((gens[k],chips[k]) for k in gens.keys()))


        return (self.e.floor,) + sig

    def __hash__(self):
        # This change here made all the difference between it
        return hash(self.sig)
        # return hash((self.floors, self.e))


    # If the state is valid
    def valid(self):
        return self.e.valid(self.floors) and all(x.valid() for x in self.floors)
    

    def score(self):
        f1, f2, f3, f4 = [10*len(x.gens) + len(x.chips) for x in self.floors]
        return 10000000 * f1 + 1000 * f2 + 10 * f3 + 1*(10*len(self.e.gens) + len(self.e.chips)) + (3-self.e.floor)*10


    def done(self):
        rooms_empty = all(len(x.gens) + len(x.chips) == 0 for x in self.floors[:-1])
        return rooms_empty and self.e.floor == (len(self.floors) - 1)

    def __repr__(self):
        return "State: {} {}".format(repr(self.floors), repr(self.e))


    def __str__(self):
        ans = ""
        for i, floor in enumerate(self.floors):
            ans += "Floor {}: Generators: {}, Chips: {}\n".format(i + 1, [x.t for x in floor.gens], [x.t for x in floor.chips])

        ans += "Elevator: Floor {}, Generators: {}, Chips: {}\n".format(self.e.floor + 1, [x.t for x in self.e.gens], [x.t for x in self.e.chips])

        return ans


    def pos_next(self):
        ans = []
        floor_items = self.floors[self.e.floor]
        elevator_items = self.e

        all_together = sorted(floor_items.gens + floor_items.chips + elevator_items.gens + elevator_items.chips)
        # assert(all(isinstance(x, Generator) for x in floor_items.gens))
        # assert(all(isinstance(x, Chip) for x in floor_items.chips))


        # Nowe we must generate every different configuration of these
        for l in range(1,3):
            for combs in it.combinations(all_together, l):
                thangs = list(all_together)



                for c in combs:
                    thangs.remove(c)
                # print(thangs)

                # assert(len(all_together) == len(thangs) + len(combs))

                upad = []

                if self.e.floor != 3:
                    upad.append(1)

                if self.e.floor != 0:
                    fwl = self.floors[self.e.floor-1]
                    if len(fwl.gens) + len(fwl.chips) != 0:
                        upad.append(-1)

                    # upad.append(-1)


                ee_gens = tuple(sorted([x for x in combs if isinstance(x, Generator)]))
                ee_chips = tuple(sorted([x for x in combs if isinstance(x, Chip)]))
                f1, f2, f3, f4 = self.floors
                fn = Floor(tuple([x for x in thangs if isinstance(x, Generator)]), tuple([x for x in thangs if isinstance(x, Chip)]))

                if not fn.valid():
                    continue

                for n in upad:
                    # if not (0 <= (self.e.floor + n) < 4):
                    #     continue


                    ee = Elevator(self.e.floor + n, ee_gens, ee_chips)

                    # fn = Floor([x for x in thangs if isinstance(x, Generator)], [x for x in thangs if isinstance(x, Chip)])

                    if not ee.valid(self.floors[ee.floor]):
                        continue


                    if self.e.floor == 0:
                        SN = State(fn, f2, f3, f4, ee)
                    elif self.e.floor == 1:
                        SN = State(f1, fn, f3, f4, ee)
                    elif self.e.floor == 2:
                        SN = State(f1, f2, fn, f4, ee)
                    elif self.e.floor ==3:
                        SN = State(f1, f2, f3, fn, ee)
                    else:
                        raise Error("WTFF")
                    # SN.floors[self.e.floor].gens = tuple(sorted([x for x in thangs if isinstance(x, Generator)]))
                    # SN.floors[self.e.floor].chips = tuple(sorted([x for x in thangs if isinstance(x, Chip)]))

                    
                    ans.append(SN)

                    # if SN.valid():
                    #     ans.append(SN)


        # if len(ans) == 0:
        #     print("===BEGIN POS NEXT ===")
        #     print(repr(self))
        #     print(self)
        #     print("=== END POS NEXT ===")
        #     assert(False)
                    
       
        return ans
    
    def __lt__(self, other):
        return self.e.floor > other.e.floor

    def pretty(self):
        ans = ""
        names = set([x.t for x in self.e.gens])
        for floor in self.floors:
            names.update([x.t for x in floor.gens])

        ma = {k: v for k, v in zip("ABCDEFLX", sorted(names))}

        fxs = []
        for i, floor in enumerate(self.floors):
            gens = [x.t for x in floor.gens]
            chips = [x.t for x in floor.chips]

            m = "F{}".format(i+1)
            if i == self.e.floor:
                gens += [x.t for x in self.e.gens]
                chips += [x.t for x in self.e.chips]
                m += " E"
            else:
                m += "  "

            for k, v in ma.items():
                if v in gens:
                    m += " G{}".format(k)
                else:
                    m += "   "

                if v in chips:
                    m += " M{}".format(k)
                else:
                    m += "   "

            fxs.append(m)

        ans += "\n".join(reversed(fxs))

        return ans


import time

def animate_it(made_it, fin):
    states = [fin]
    while states[-1] in made_it:
        states.append(made_it[states[-1]])

    states = reversed(states)

    for i, state in enumerate(states):
        # print(chr(27) + "[2J")
        print("\033c", end="")
        print("=== STATE {} ===".format(i))
        print(state.pretty())
        time.sleep(0.5)


# S is the state
def solve_smart(S: State):
    # Q = collections.deque([(S, 0)])
    Q = [(S.score(), 0, S)]
    # Q = [(S, 0)]

    got_it = collections.defaultdict(lambda: 3000000000000)
    got_it[S] = 0
    seen = set()
    max_depth = 0
    min_find = 10000000000000000000000000000000
    made_it = {}
    while len(Q) > 0:
        _, depth, qs = heapq.heappop(Q)
        # if max_depth < 13:
        #     qs, depth = Q.popleft()
        # else:
        #     qs, depth = Q.pop()

        # seen.add(qs)
        
        if depth + 1 >= min_find: #or depth+1 > 50:
            continue

        if depth > max_depth:
            print("new max depth of: {}".format(depth))
            max_depth = depth
        # print("new depth of: {}".format(depth))

        added = 0
        new = qs.pos_next()
        for newq in new:
            # we keep track of the minimal score to get here
            if got_it[newq] > (depth + 1):
                got_it[newq] = depth + 1
                made_it[newq] = qs
            else:
                continue

            if newq.done():
                if depth + 1 < min_find:
                    min_find = depth + 1
                    print("New min_find: {}".format(min_find))
                    # animate_it(made_it, newq)

            # if depth:
            added += 1
            # Q.append((newq, depth + 1))
            # heapq.heappush(Q, (newq.score(), depth + 1, newq))
            heapq.heappush(Q, ((depth + 1) * 100 +  newq.score(), depth + 1, newq))
            # Q.append((newq, depth + 1))
                # nextQ.append((newq, depth + 1))
            # else:
            #     # print(" we have a duep")
            #     pass

        # if added == 0:
        #     print("We added none")

    return min_find


test1 = State(
    Floor([], [Chip("hydrogen", "c"), Chip("lithium", "c")]), # F1
    Floor([Generator("hydrogen", "g")], []),
    Floor([Generator("lithium", "g")], []),
    Floor([], []),
    Elevator(0, [], []),
)


# The first floor contains a promethium generator and a promethium-compatible microchip.
# The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
# The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
# The fourth floor contains nothing relevant.

real1 = State(
    Floor(tuple([Generator("promethium", "g")]), tuple([Chip("promethium", "c")])),
    Floor((Generator("cobalt", "g"), Generator("curium", "g"), Generator("ruthenium", "g"), Generator("plutonium", "g")), ()),
    Floor((), (Chip("cobalt", "c"), Chip("curium", "c"), Chip("ruthenium", "c"), Chip("plutonium", "c"))),
    Floor((), ()),
    Elevator(0, (), ()),
)

real2 = State(
    Floor((Generator("elerium", "g"), Generator("promethium", "g"), Generator("dilithium", "g")), (Chip("promethium", "c"), Chip("elerium", "c"), Chip("dilithium", "c"))),
    Floor((Generator("cobalt", "g"), Generator("curium", "g"), Generator("ruthenium", "g"), Generator("plutonium", "g")), ()),
    Floor((), (Chip("cobalt", "c"), Chip("curium", "c"), Chip("ruthenium", "c"), Chip("plutonium", "c"))),
    Floor((), ()),
    Elevator(0, (), ()),
)

# b = copy.deepcopy(test1)
# k = set()

# print(solve_smart(test1))
print(solve_smart(real1))
# print(solve_smart(real2))
