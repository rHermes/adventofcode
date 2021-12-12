import fileinput as fi
import math
import collections as cs
import heapq
import itertools as it

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

Point = tuple[int,int]
# pos, type, attack power, hp, id
Entity = tuple[Point,str,int,int,int]
Board = list[list[bool]]

lines = [x.rstrip() for x in fi.input()]

def parse_input(n: int) -> tuple[list[Entity], Board]:
    ents = []
    board = []
    wi = it.count()
    for y, line in enumerate(lines):
        row = []
        for x, c in enumerate(line):
            if c == '#':
                row.append(True)
            else:
                row.append(False)

            if c in "EG":
                ents.append(((y,x),c,[3, n][c == "E"],200,next(wi)))
                
        board.append(row)
    
    return ents, board


def estima(src: Point, in_range: set[Point]) -> int:
    """estimate the cost of getting to a point"""
    min_cost = 10000000000000000000000000000
    for dst in in_range:
        cost = abs(dst[0] - src[0]) + abs(dst[1] - src[1])
        if cost < min_cost:
            min_cost = cost

    return min_cost

# This returns the set of points to consider.
def reachable(board: Board, src: Point, taken: set[Point], in_range: set[Point]) -> set[tuple[int,Point]]:
    # We just find the ones that are reachable

    Q = cs.deque([(0, src)])
    seen = set(taken)
    found = set()

    best_depth = 10000000000000000
    while len(Q) > 0:
        depth, cur = Q.popleft()
        if best_depth < depth:
            continue

        if cur in seen:
            continue
        else:
            seen.add(cur)


        if cur in in_range:
            if depth < best_depth:
                best_depth = depth
                gprint("We have a new best depth:", best_depth)

            found.add((depth,cur))


        y, x = cur
        for dy, dx in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            ty, tx = y + dy, x + dx
            if not board[ty][tx] and (ty,tx) not in taken and (ty,tx) not in seen:
                Q.append((depth + 1, (ty,tx)))
    

    gprint("We assume the reachables are:", found)

    gprint(found)

    return found


def pick_move(board: Board, src: Point, taken: set[Point], in_range: set[Point]) -> Point:
    """Pick the move to make in a situation"""
    if src in in_range:
        gprint("already in range")
        return src

    reachs = reachable(board, src, taken, in_range)
    if len(reachs) == 0:
        gprint("There is no reach")
        return src
    
    dap, dst = min(reachs)
    gprint("our dest is:", dst)

    # We attempt each point around to see the length.
    # depth, start, cur
    Q: list[tuple[int,Point,Point]] = []
    for dy, dx in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
        ty, tx = src[0] + dy, src[1] + dx
        if not board[ty][tx] and (ty,tx) not in taken:
            heapq.heappush(Q, (1, (ty,tx), (ty, tx)))
            # in_range.add((ty,tx))

    seen = set()
    while len(Q) > 0:
        depth, start, cur = heapq.heappop(Q)
        if cur in seen:
            continue
        else:
            seen.add(cur)

        if cur == dst:
            return start

        for dy, dx in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            ty, tx = cur[0] + dy, cur[1] + dx
            if not board[ty][tx] and (ty,tx) not in taken and (ty,tx) not in seen:
                heapq.heappush(Q, (depth + 1, start, (ty,tx)))

    
    raise Exception("Not supposed to reach here")
        


    # new_loc = src
    # return new_loc

# DEBUG = False

def turn(board: Board, ents: list[Entity], ent: Entity):
    targets = [e for e in ents if e[1] != ent[1]]
    if len(targets) == 0:
        ents.append(ent)
        return

    taken = set([e[0] for e in ents])

    in_range = set()
    for target in targets:
        y, x = target[0]
        for dy, dx in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            ty, tx = y + dy, x + dx
            if not board[ty][tx] and (ty,tx) not in taken:
                in_range.add((ty,tx))

    gprint("=== START ===")
    gprint("ent:", ent)
    gprint("targets:", targets)
    gprint("in_range:", in_range)

    ny, nx = pick_move(board, ent[0], taken, in_range)

    if (ny,nx) in in_range:
        to_attack = []
        for dy, dx in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            ty, tx = ny + dy, nx + dx
            for target in targets:
                if target[0] == (ty, tx):
                    to_attack.append((target[3], target))

        assert(len(to_attack) > 0)
        _, will_attack = min(to_attack)
        gprint("Will attack:", will_attack)
        ents.remove(will_attack)
        new_ent = will_attack[:3] + (will_attack[3] - ent[2],) + will_attack[4:]
        assert(len(new_ent) == len(will_attack))
        if new_ent[3] <= 0:
            gprint("A unit died!")
        else:
            ents.append(new_ent)


    # We make the move and insert the entity again.
    ents.append(((ny,nx),) + ent[1:])
    gprint("=== END ===")


def one_round(board: Board, ents: list[Entity]):
    # These return the board and the ents.
    order = [e[-1] for e in sorted(ents)]
    for eid in order:
        # This might be slow, but it will do for now
        for ent in ents:
            if eid == ent[-1]:
                break
        else:
            gprint("This was a dead entry")
            continue

        # This might be slow, but  IDC
        if sum(1 for e in ents if e[1] != ent[1]) == 0:
            return False
    
        # We remove it from the entry list, as we will now
        # move it.
        ents.remove(ent)

        # This will modify the ents array
        turn(board, ents, ent)

        # For now we break, as we don't insert stuff again.
    return True

def print_board(board: Board, ents: list[Entity]):
    ogres = set(e[0] for e in ents if e[1] == "G")
    elves = set(e[0] for e in ents if e[1] == "E")
    ns = []
    for y, row in enumerate(board):
        nn = ""
        for x, c in enumerate(row):
            if board[y][x]:
                nn += "#"
            elif (y,x) in ogres:
                nn += "G"
            elif (y,x) in elves:
                nn += "E"
            else:
                nn += "."

        ns.append(nn)

    print("\n".join(ns))

def go_for_it(n: int):
    ents, board = parse_input(n)
    # print(ents)
    # print("Initially:")
    # print_board(board, ents)
    n_elves_start = sum(1 for e in ents if e[1] == "E")
    # print("start elves:", n_elves_start)
    gad = 1
    for i in it.count(0):
        if sum(1 for e in ents if e[1] == "E") < n_elves_start:
            return False
        
        # print("After {} round:".format(i))
        # print_board(board, ents)
        if len(ents) == n_elves_start:
            break

        gad = one_round(board, ents)
        # print(ents)
        # print("")

    if not gad:
        i -= 1
    # print(gad)
    # print(ents)
    print("It ended after {} rounds with an outcome of {}".format(i, i*sum(e[3] for e in ents)))
    return True

DEBUG = False
for i in it.count(4):
    # print(i)
    x = go_for_it(i)
    if x:
        break
