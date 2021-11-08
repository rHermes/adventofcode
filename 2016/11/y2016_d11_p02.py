from __future__ import annotations

import fileinput as fi
import re
import itertools as it
import collections

import heapq

import attr
import typing


@attr.s(auto_attribs=True, frozen=False)
class Floor:
    gens: typing.FrozenSet[str] = attr.Factory(frozenset)
    chips: typing.FrozenSet[str]  = attr.Factory(frozenset)

    def valid(self) -> bool:
        return len(self.gens) == 0 or len(self.chips - self.gens) == 0


@attr.s(auto_attribs=True, frozen=False, eq=False)
class State():
    floors: typing.Tuple[Floor, Floor, Floor, Floor]
    cur: int = 0

    sig: typing.Optional[typing.Tuple[int, typing.Tuple[typing.Tuple[int, int], ...]]] = None

    def signature(self) -> typing.Tuple[int, typing.Tuple[typing.Tuple[int, int], ...]]:
        if self.sig is not None:
            return self.sig

        gens = {}
        chips = {}
        for i, floor in enumerate(self.floors):
            for x in floor.gens:
                gens[x] = i

            for y in floor.chips:
                chips[y] = i

        sig = tuple(sorted((gens[k], chips[k]) for k in gens.keys()))

        self.sig = (self.cur, sig)

        return self.sig

    def __eq__(self, other) -> bool:
        if not isinstance(other, type(self)): return NotImplemented
        return self.signature() == other.signature()
        # return self.sig == other.sig

    def __hash__(self) -> int:
        # This change here made all the difference between it
        return hash(self.signature())


    # If the state is valid
    def valid(self) -> bool:
        return 0 <= self.cur < len(self.floors) and all(x.valid() for x in self.floors)

    def score(self) -> int:
        f1, f2, f3, f4 = [10*len(x.gens) + len(x.chips) for x in self.floors]
        return 100000 * f1 + 10000 * f2 + 10 * f3 + (len(self.floors)-1-self.cur)*10


    def done(self) -> bool:
        if self.cur != len(self.floors)-1:
            return False

        rooms_empty = all(len(x.gens) + len(x.chips) == 0 for x in self.floors[:-1])
        return rooms_empty

    def pos_next(self) -> typing.List[State]:
        ans = []
        floor_items = self.floors[self.cur]

        for l in range(0, 3):
            for jp in range(0, 3-l):
                if l + jp == 0:
                    continue

                gg = it.combinations(floor_items.gens, l)
                ff = it.combinations(floor_items.chips, jp)

                for negens, nechips in it.product(gg, ff):
                    egens = frozenset(negens)
                    echips = frozenset(nechips)

                    current_floor = Floor(floor_items.gens - egens, floor_items.chips - echips)

                    if not current_floor.valid():
                        continue

                    upad = []
                    if self.cur != len(self.floors)-1:
                        upad.append(1)

                    if self.cur != 0:
                        # Optimization here, where we never go down to an empty floor
                        below = self.floors[self.cur-1]
                        if len(below.gens) + len(below.chips) > 0:
                            upad.append(-1)


                    for n in upad:
                        un = self.cur + n
                        new_floor = Floor(self.floors[un].gens | egens, self.floors[un].chips | echips)
                        if not new_floor.valid():
                            continue

                        wow = list(self.floors)
                        wow[self.cur] = current_floor
                        wow[un] = new_floor
                        SN = State((wow[0], wow[1], wow[2], wow[3]), un)

                        ans.append(SN)

        return ans


    def __lt__(self, other) -> bool:
        return self.cur > other.cur

    def pretty(self) -> str:
        ans = ""
        names: typing.Set[str] = set()
        for floor in self.floors:
            names.update([x for x in floor.gens])

        ma = {k: v for k, v in zip("ABCDEFLX", sorted(names))}

        fxs = []
        for i, floor in enumerate(self.floors):
            gens = [x for x in floor.gens]
            chips = [x for x in floor.chips]

            m = "F{}".format(i+1)
            if i == self.cur:
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

def animate_it(made_it: typing.Dict[State, State], fin: State):
    states = [fin]
    while states[-1] in made_it:
        states.append(made_it[states[-1]])

    rev_states = reversed(states)

    for i, state in enumerate(rev_states):
        # print(chr(27) + "[2J")
        print("\033c", end="")
        print("=== STATE {} ===".format(i))
        print(state.pretty())
        time.sleep(0.1)


# S is the state
def solve_smart(S: State):
    Q = [(S.score(), 0, S)]

    got_it = collections.defaultdict(lambda: 3000000000000)
    got_it[S] = 0

    min_find = 10000000000000000000000000000000
    made_it = {}
    while len(Q) > 0:
        _, depth, qs = heapq.heappop(Q)
        if depth + 1 >= min_find:
            continue

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
                    # print("New min_find: {}".format(min_find))
                    # animate_it(made_it, newq)

            heapq.heappush(Q, ((depth + 1) * 100 +  newq.score(), depth + 1, newq))

    return min_find


test1 = State(
    (
    Floor(frozenset([]), frozenset(["hydrogen", "lithium"])), # F1
    Floor(frozenset(["hydrogen"]), frozenset([])),
    Floor(frozenset(["lithium"]), frozenset([])),
    Floor(frozenset([]), frozenset([])),
    ),
)


# The first floor contains a promethium generator and a promethium-compatible microchip.
# The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
# The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
# The fourth floor contains nothing relevant.

real1 = State(
    (
    Floor(frozenset(["promethium"]), frozenset(["promethium"])),
    Floor(frozenset((("cobalt"), ("curium"), ("ruthenium"), ("plutonium"))), frozenset()),
    Floor(frozenset(), frozenset((("cobalt"), ("curium"), ("ruthenium"), ("plutonium")))),
    Floor(frozenset(), frozenset()),
    )
)

real2 = State(
    (
    Floor(frozenset(("elerium", "promethium", "dilithium")), frozenset(("promethium", "elerium", "dilithium"))),
    Floor(frozenset((("cobalt"), ("curium"), ("ruthenium"), ("plutonium"))), frozenset()),
    Floor(frozenset(), frozenset((("cobalt"), ("curium"), ("ruthenium"), ("plutonium")))),
    Floor(frozenset(), frozenset()),
    )
)


# print(solve_smart(test1))
# print(solve_smart(real1))
print(solve_smart(real2))
