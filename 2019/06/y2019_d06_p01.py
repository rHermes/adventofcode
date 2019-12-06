import fileinput


G = {}
for line in fileinput.input():
    a, b = line.rstrip().split(")")
    G[b] = a


ans = 0
for node in G.keys():
    indirect = 0
    cur = node
    while (G[cur] in G):
        indirect += 1
        cur = G[cur]
    
    ans += indirect

print(ans + len(G.keys()))
