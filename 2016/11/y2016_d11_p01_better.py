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
        self.gens = tuple(sorted(generators))
        self.chips = tuple(sorted(chips))

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
        self.gens = tuple(sorted(generators))
        self.chips = tuple(sorted(chips))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.floor == other.floor and self.gens == other.gens and self.chips == other.chips

    def __hash__(self):
        return hash((self.floor, self.gens, self.chips))

    def __repr__(self):
        return "Elevator: {} {} {}".format(repr(self.floor), repr(self.gens), repr(self.chips))


    def valid(self, floors):
        return 0 <= self.floor < 4 and Floor(self.gens + floors[self.floor].gens, self.chips + floors[self.floor].chips).valid()



class State():
    def __init__(self, floor1, floor2, floor3, floor4, elevator):
        self.floors = (floor1, floor2, floor3, floor4)
        self.e = elevator

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.floors == other.floors and self.e == other.e

    def __hash__(self):
        return hash((self.floors, self.e))


    # If the state is valid
    def valid(self):
        return self.e.valid(self.floors) and all(x.valid() for x in self.floors)
    

    def score(self):
        f1, f2, f3, f4 = [10*len(x.gens) + len(x.chips) for x in self.floors]
        return 1000000 * f1 + 100000 * f2 + 10 * f3 + 1*(10*len(self.e.gens) + len(self.e.chips))


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
                if self.e.floor != 0:
                    upad.append(-1)

                if self.e.floor != 3:
                    upad.append(1)


                ee_gens = sorted([x for x in combs if isinstance(x, Generator)])
                ee_chips = sorted([x for x in combs if isinstance(x, Chip)])
                f1, f2, f3, f4 = self.floors
                fn = Floor([x for x in thangs if isinstance(x, Generator)], [x for x in thangs if isinstance(x, Chip)])

                for n in upad:
                    # if not (0 <= (self.e.floor + n) < 4):
                    #     continue


                    ee = Elevator(self.e.floor + n, ee_gens, ee_chips)
                    # fn = Floor([x for x in thangs if isinstance(x, Generator)], [x for x in thangs if isinstance(x, Chip)])

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

                    if SN.valid():
                        ans.append(SN)


        if len(ans) == 0:
            print("===BEGIN POS NEXT ===")
            print(repr(self))
            print(self)
            print("=== END POS NEXT ===")
            assert(False)
                    
       
        return ans
    
    def __lt__(self, other):
        return self.e.floor > other.e.floor



import tqdm


# S is the state
def solve(S: State):
    Q = collections.deque([(S, 0)])
    # Q = [(S, 0)]

    got_it = collections.defaultdict(lambda: 3000000000000)
    got_it[S] = 0
    seen = set()
    max_depth = 0
    min_find = 10000000000000000000000000000000
    while len(Q) > 0:
        if max_depth < 13:
            qs, depth = Q.popleft()
        else:
            qs, depth = Q.pop()

        # seen.add(qs)
        
        if depth + 1 >= min_find:
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
            else:
                continue

            if newq.done():
                if depth + 1 < min_find:
                    min_find = depth + 1
                    print("New min_find: {}".format(min_find))

            # if depth:
            added += 1
            Q.append((newq, depth + 1))
                # nextQ.append((newq, depth + 1))
            # else:
            #     # print(" we have a duep")
            #     pass

        # if added == 0:
        #     print("We added none")

    return min_find
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


# real = State(
#     Floor([Generator("elerium", "g"), Generator("promethium", "g"), Generator("dilithium", "g")], [Chip("promethium", "c"), Chip("elerium", "c"), Chip("dilithium", "c")]),
#     Floor([Generator("cobalt", "g"), Generator("curium", "g"), Generator("ruthenium", "g"), Generator("plutonium", "g")], []),
#     Floor([], [Chip("cobalt", "c"), Chip("curium", "c"), Chip("ruthenium", "c"), Chip("plutonium", "c")]),
#     Floor([], []),
#     Elevator(0, [], []),
# )
real = State(
    Floor([Generator("promethium", "g")], [Chip("promethium", "c")]),
    Floor([Generator("cobalt", "g"), Generator("curium", "g"), Generator("ruthenium", "g"), Generator("plutonium", "g")], []),
    Floor([], [Chip("cobalt", "c"), Chip("curium", "c"), Chip("ruthenium", "c"), Chip("plutonium", "c")]),
    Floor([], []),
    Elevator(0, [], []),
)

# b = copy.deepcopy(test1)
# k = set()

# print(solve_smart(test1))
print(solve_smart(real))
