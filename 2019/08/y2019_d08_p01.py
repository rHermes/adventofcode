import fileinput
from collections import Counter

def solve(s):
    dims = len(s)//(25*6)
    
    minn = 9999999999999
    minx = -1 

    for i in range(dims):
        k = s[i*(25*6):(i+1)*(25*6)]
        
        c = Counter(k)
        if c["0"] < minn:
            minn = c["0"]
            minx = c["1"] * c["2"]

    return minx


for line in fileinput.input():
    print(solve(line.strip()))
