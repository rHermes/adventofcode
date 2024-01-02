import fileinput as fi
import random
import collections as cs
import copy

# Parse input
G = cs.defaultdict(lambda: cs.defaultdict(set))
for line in fi.input():
    src, *dsts = line.replace(":", "").split()
    for dst in dsts:
        mmin, mmax = min(src, dst), max(src, dst)
        G[src][dst].add((mmin,mmax))
        G[dst][src].add((mmin,mmax))


def contract(G, until):
    graph = copy.deepcopy(G)
    while until < len(graph):
        start, rest = random.choice(list(graph.items()))
        end, _ = random.choice(list(rest.items()))
        # print("First we are merging {} and {}".format(start, end))

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
        # print("wow")
        return contract(G, 2)
    else:
        # t = math.ceil(1 + len(G)/math.sqrt(2))
        # t = math.ceil(len(G)/2.1)
        t = len(G) // 2.1 
        # print(t)
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


    


# To pin the value for now
random.seed(1)

mincut = 1000000000000000000000000000000000
bestcut = set()
while True:
    gr = fastmincut(G)
    bw, aw = gr.keys()
    cut = gr[bw][aw]
    if len(cut) < mincut:
        mincut = len(cut)
        bestcut = cut
        print(bestcut)
        if mincut == 3:
            break

# print(bestcut)
