import fileinput
import collections

# Returns the graph, src and dst
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


    # Inner and outer
    portals_o = {}
    portals_i = {}

    # We must collect the ones at the edges
    for y, row in enumerate(board):
        if row[:2] != "  ":
            portals_o[row[:2]] =  (0, y-2)

        if row[-2:] != "  ":
            portals_o[row[-2:]] =  (W-4-1, y-2)

        if inner_start_y < y <  inner_end_y:
            # These are the inner ring
            tt = row[inner_start_x:inner_start_x+2]
            if tt != "  ":
                portals_i[tt] = (inner_start_x-1-2, y-2)

            # On the outer ring
            tt = row[inner_end_x-2:inner_end_x]
            if tt != "  ":
                portals_i[tt] = (inner_end_x-2, y-2)

    for x in range(2, W-2):
        if board[0][x] != " ":
            kk = board[0][x] + board[1][x]
            portals_o[kk] = (x-2, 0)

        if board[H-2][x] != " ":
            kk = board[H-2][x] + board[H-1][x]
            portals_o[kk] = (x-2, H-4-1)

        if inner_start_x < x < inner_end_x:
            # Inner ring
            if board[inner_start_y][x] != " ":
                kk = board[inner_start_y][x] + board[inner_start_y+1][x]
                portals_i[kk] = (x-2, inner_start_y-1-2)

            if board[inner_end_y-2][x] != " ":
                kk = board[inner_end_y-2][x] + board[inner_end_y-1][x]
                portals_i[kk] = (x-2, inner_end_y-2)


    paths = set()
    for y in range(2,H-2):
        for x in range(2, W-2):
            if board[y][x] == ".":
                paths.add((x-2,y-2))

    # I just assume that this will be enough
    #Z = len(portals_o)
    Z = len(portals_o)
    # Let's create the depth
    G = collections.defaultdict(set)
    for z in range(0, Z):
        for (x,y) in paths:
            dirs = [(x,y-1), (x+1,y), (x,y+1), (x-1, y)]
            for d in dirs:
                if d in paths:
                    G[(z,x,y)].add((z,d[0],d[1]))

        # Portal mapping
        # Outer portals
        if z > 0:
            for p, pt in portals_o.items():
                if p not in portals_i:
                    continue
                pd = portals_i[p]

                # Add z
                pt = (z,pt[0],pt[1])
                pd = (z-1, pd[0], pd[1])

                G[pt].add(pd)
                G[pd].add(pt)

        # Inner portals
        if z < Z:
            for p, pt in portals_i.items():
                pd = portals_o[p]

                # Add z
                pt = (z,pt[0],pt[1])
                pd = (z+1, pd[0], pd[1])

                G[pt].add(pd)
                G[pd].add(pt)


    src = portals_o["AA"]
    src = (0, src[0], src[1])
    dst = portals_o["ZZ"]
    dst = (0, dst[0], dst[1])
    return G, src, dst


# Simple BFS search
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
    print("No path to answer")
