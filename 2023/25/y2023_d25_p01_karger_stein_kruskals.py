import fileinput as fi
import random

class DSU(object):
    def __init__(self):
        self.sizes = {}
        self.parents = {}

    def MakeSet(self, x):
        if x in self.parents:
            return

        self.parents[x] = x
        self.sizes[x] = 1

    def Find(self, x):
        """Finds the root parent for an element"""
        s = self.parents[x]

        if x != s:
            self.parents[x] = self.Find(s)
            return self.parents[x]
        else:
            return x
    
    def Union(self, x, y):
        """Add the two items into the same group"""
        x = self.parents[x]
        y = self.parents[y]

        if x == y:
            return

        xs = self.sizes[x]
        ys = self.sizes[y]

        if xs < ys:
            x, y = y, x
        
        self.parents[y] = x
        self.sizes[x] += self.sizes[y]

    def Size(self, x):
        a = self.Find(x)
        return self.sizes[a]
        

def krushal(V: set[str], E: list[tuple[str,str]], doUntil=2):
    D = DSU()
    for v in V:
        D.MakeSet(v)
        
    ans = 0
    rest = len(V)
    for u, v in E:
        a = D.Find(u)
        b = D.Find(v)

        if a != b:
            rest -= 1
            if rest < doUntil:
                ans = D.Size(a) * D.Size(b)
                break

            D.Union(a, b)

    
    numCuts = 0
    for u, v in E:
        a = D.Find(u)
        b = D.Find(v)

        if a != b:
            numCuts += 1
    
    return (numCuts, ans)

# Parse input
V = set()
E = []
for line in fi.input():
    src, *dsts = line.replace(":", "").split()
    V.add(src)
    V.update(dsts)
    for dst in dsts:
        mmin, mmax = min(src, dst), max(src, dst)
        E.append((mmin,mmax))

while True:
    numCuts, ans = krushal(V, E)
    if numCuts <= 3:
        print(ans)
        break

    random.shuffle(E)

