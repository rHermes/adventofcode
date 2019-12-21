import fileinput
import collections


def parse_board(board):
    W = len(board[0])
    H = len(board)

    # This finds the topografy as the works
    # We must figure out inner points
    for inner_start_y in range(2, H-2):
        if board[inner_start_y][W//2] not in [".", "#"]:
            break

    for inner_end_y in range(inner_start_y, H-2):
        if board[inner_end_y][W//2] in [".", "#"]:
            # inner_end_y -= 1
            break

    for inner_start_x in range(2, W-2):
        if board[inner_start_y][inner_start_x] not in [".", "#"]:
            break

    for inner_end_x in range(inner_start_x, W-2):
        if board[inner_start_y][inner_end_x] in [".", "#"]:
            # inner_end_x -= 1
            break

    portals = {}

    # We must collect the ones at the edges
    for y, row in enumerate(board):
        if row[:2] != "  ":
            portals[row[:2]] =  portals.get(row[:2], []) + [(0, y-2)]

        if row[-2:] != "  ":
            portals[row[-2:]] =  portals.get(row[-2:], []) + [(W-4-1, y-2)]

        if inner_start_y < y <  inner_end_y:
            # These are the inner ring
            tt = row[inner_start_x:inner_start_x+2]
            if tt != "  ":
                portals[tt] = portals.get(tt, []) + [(inner_start_x-1-2, y-2)]

            # On the outer ring
            tt = row[inner_end_x-2:inner_end_x]
            if tt != "  ":
                portals[tt] = portals.get(tt, []) + [(inner_end_x-2, y-2)]

    for x in range(2, W-2):
        if board[0][x] != " ":
            kk = board[0][x] + board[1][x]
            portals[kk] = portals.get(kk, []) + [(x-2, 0)]

        if board[H-2][x] != " ":
            kk = board[H-2][x] + board[H-1][x]
            portals[kk] = portals.get(kk, []) + [(x-2, H-4-1)]

        if inner_start_x < x < inner_end_x:
            # Inner ring
            if board[inner_start_y][x] != " ":
                kk = board[inner_start_y][x] + board[inner_start_y+1][x]
                portals[kk] = portals.get(kk, []) + [(x-2, inner_start_y-1-2)]

            if board[inner_end_y-2][x] != " ":
                kk = board[inner_end_y-2][x] + board[inner_end_y-1][x]
                portals[kk] = portals.get(kk, []) + [(x-2, inner_end_y-2)]

    paths = set()
    for y in range(2,H-2):
        for x in range(2, W-2):
            if board[y][x] == ".":
                paths.add((x-2,y-2))


    # Now we can create the graph
    G = collections.defaultdict(set)
    for (x,y) in paths:
        dirs = [(x,y-1), (x+1,y), (x,y+1), (x-1, y)]
        for d in dirs:
            if d in paths:
                G[(x,y)].add(d)

    # Create the portal mappings
    for p, ps in portals.items():
        if len(ps) < 2:
            continue
        assert(len(ps) == 2)

        G[ps[0]].add(ps[1])
        G[ps[1]].add(ps[0])

    # Return G, start, end
    return G, portals["AA"][0], portals["ZZ"][0]



def route_to(G, src, dst):
    Q = collections.deque()
    seen = set(src)
    prev = {}
    Q.append(src)

    while len(Q) > 0:
        v = Q.popleft()
        if v == dst:
            # Create this here
            path = [dst]
            while path[0] in prev and path[0] != src:
                path.insert(0,prev[path[0]])

            return path

        for w in G[v]:
            if w not in seen:
                seen.add(w)
                prev[w] = v
                Q.append(w)

board = []
for line in fileinput.input():
    board.append(line[:-1])


G, src, dst = parse_board(board)
path = route_to(G, src, dst)
if path:
    print("{}".format(len(path)-1))
else:
    print("No answer")
