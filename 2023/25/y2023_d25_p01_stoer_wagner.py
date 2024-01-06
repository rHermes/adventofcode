import fileinput as fi

# You need to run this in pypy or it will never finished!

# Parse input
E = []
compress = {}
for line in fi.input():
    src, *dsts = line.replace(":", "").split()
    if src not in compress:
        compress[src] = len(compress)

    isrc = compress[src]
    for dst in dsts:
        if dst not in compress:
            compress[dst] = len(compress)

        idst = compress[dst]
        E.append((isrc,idst))

# We have stolen this directly from wikipedia, shame on me.
# I tried to get an alternative implementation going, but I couldn't
# do it. I'll try again for this later on maybe.
def minimum_cut(mat):
    N = len(mat)
    best = (10000000000000000000, {})
    co = [set([i]) for i in range(N)]

    # I don't know why this is needed, but it is.
    INT_MIN = -100000000000000000000

    # We are going to iterate until there are only 2 verticies left total.
    for ph in range(1, N):
        w = list(mat[0])
        s = 0
        t = 0
        for it in range(0, N - ph):
            # We make sure the current weight will never be considered the best
            w[t] = INT_MIN

            s = t
            t = max(range(N), key=w.__getitem__)

            # Now that we have decided to include the item t, we are going to
            # add all it's edges to the graph
            for i in range(0, N):
                w[i] += mat[t][i]

        # Nowe we have s and t, and we want to know what is best
        # We have to remove mat[t][t], because we add it to w[t]
        # in the step above
        pv = (w[t] - mat[t][t], co[t])
        if pv < best:
            best = pv

        co[s].update(co[t])

        for i in range(N):
            mat[s][i] += mat[t][i]

        for i in range(N):
            mat[i][s] = mat[s][i]

        # I don't know why we need to set it to negative, but we get
        # false positives without it
        mat[0][t] = INT_MIN

    return best


# Convert it to an adjancency matrix.
N = len(compress)
mat = []
for _ in range(N):
    mat.append([0 for _ in range(N)])

for src, dst in E:
    mat[src][dst] = 1
    mat[dst][src] = 1


mc = minimum_cut(mat)
print(len(mc[1]) * (N - len(mc[1])))
