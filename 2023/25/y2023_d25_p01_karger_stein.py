import fileinput as fi
import random
import collections as cs

# Parse input
G = cs.defaultdict(lambda: cs.defaultdict(set))
for line in fi.input():
    src, *dsts = line.replace(":", "").split()
    for dst in dsts:
        mmin, mmax = min(src, dst), max(src, dst)
        G[src][dst].add((mmin,mmax))
        G[dst][src].add((mmin,mmax))


def contract(G, until):
    # deepcopy is very slow for this task, so we implement the copying
    # by hand.
    graph = cs.defaultdict(lambda: cs.defaultdict(set))
    for node, rest in G.items():
        for dst, vals in rest.items():
            graph[node][dst] = set(vals)

    while until < len(graph):
        start, rest = random.choice(list(graph.items()))
        end, _ = random.choice(list(rest.items()))

        for node, connections in rest.items():
            if node == end:
                continue

            graph[end][node].update(connections)
            graph[node][end].update(connections)

            del graph[node][start]
            if len(graph[node]) == 0:
                del graph[node]


        # Now we remove the start node
        del graph[start]
        del graph[end][start]
    
    return graph


def fastmincut(G):
    if len(G) <= 6:
        return contract(G, 2)
    else:
        ## This treshold was found via experimentation to be
        ## orders of magnitude better than the limit given on the wikipedia page.
        # t = math.ceil(1 + len(G)/math.sqrt(2))
        # t = math.ceil(len(G)/2.1)
        t = len(G) // 2.1 
        G1 = contract(G, t)
        G2 = contract(G, t)

        fm1 = fastmincut(G1)
        fm1a, fm1b = fm1.keys()
        fm1cut = fm1[fm1a][fm1b]

        fm2 = fastmincut(G2)
        fm2a, fm2b = fm2.keys()
        fm2cut = fm2[fm2a][fm2b]

        if len(fm1cut) < len(fm2cut):
            return fm1
        else:
            return fm2

def subgraph_size(G, start):
    seen = set()
    Q = cs.deque([start])
    while Q:
        node = Q.pop()
        if node in seen:
            continue
        else:
            seen.add(node)

        for dst in G[node].keys():
            if dst not in seen:
                Q.append(dst)

    return len(seen)


mincut = 1000000000000000000000000000000000
bestcut = set()
while True:
    gr = fastmincut(G)
    bw, aw = gr.keys()
    cut = gr[bw][aw]
    if len(cut) < mincut:
        mincut = len(cut)
        bestcut = cut
        if mincut == 3:
            break

# We modify the graph to split it
for a, b in bestcut:
    del G[a][b]
    del G[b][a]

# We know these two must be in two different subgraphs.
a, b = bestcut.pop()
print(subgraph_size(G, a) * subgraph_size(G, b))
