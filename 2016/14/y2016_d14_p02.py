import fileinput as fi
from collections import deque

import hashlib

def stream(salt):
    i = 0
    while True:
        start = salt + str(i)
        for _ in range(2017):
            start = hashlib.md5(start.encode("latin1")).hexdigest()

        yield start
        i += 1

# Create The hashes
salt = next(fi.input()).rstrip()
hashes = stream(salt)

q = deque(x for _, x in zip(range(1000), hashes))
idx = 0
keys = []

while len(keys) < 64:
    hsh = q.popleft()
    q.append(next(hashes))

    for i in range(len(hsh)-2):
        if hsh[i] == hsh[i+1] == hsh[i+2]:
            needle = hsh[i] * 5
            for h in q:
                if needle in h:
                    keys.append(idx)
                    break

            break

    idx += 1

print(keys[-1])
