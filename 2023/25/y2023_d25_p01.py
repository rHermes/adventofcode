import fileinput as fi
import collections as cs
import random
from dataclasses import dataclass

@dataclass
class DSUSet:
    parent: str
    size: int = 1


class DSU(object):
    def __init__(self):
        self.sets = {}

    def MakeSet(self, x):
        if x in self.sets:
            return

        self.sets[x]  = DSUSet(x)

    def Find(self, x):
        """Finds the root parent for an element"""
        s = self.sets[x]

        if s.parent != x:
            s.parent = self.Find(s.parent)
            return s.parent
        else:
            return x
    
    def Union(self, x, y):
        """Add the two items into the same group"""
        x = self.Find(x)
        y = self.Find(y)

        if x == y:
            return

        a = self.sets[x]
        b = self.sets[y]

        if a.size < b.size:
            a, b = b, a
            x, y = y, x

        b.parent = x
        a.size += b.size

    def Size(self, x):
        a = self.Find(x)
        return self.sets[a].size
        

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

                # D.Union(a, b)
                break

            D.Union(a, b)

    
    numCuts = 0
    for u, v in E:
        a = D.Find(u)
        b = D.Find(v)

        if a != b:
            numCuts += 1
    
    # print(numCuts)
    return (numCuts, ans)

# def fastmincut(V

def print_dot_tree(E, F):
    print("graph G {")
          # }
    for u, v in E:
        # if (u, v) == F[-1]:
        #     print ("\t{} -- {} [color=\"orange\", penwidth=2.0]".format(u, v))
        if (u, v) in F:
            print ("\t{} -- {} [color=\"red\", penwidth=2.0]".format(u, v))
        else:
            print("\t{} -- {}".format(u, v))

    print("}")



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


# To pin the value for now
random.seed(1)

EE = list(E)
while True:
    random.shuffle(EE)
    numCuts, ans = krushal(V, EE)
    if numCuts <= 3:
        print(ans)
        break
