import fileinput as fi
import itertools as it
import hashlib

key = next(fi.input()).strip().encode("latin-1")
m = hashlib.md5(key)

for i in map(str, it.count(1)):
    mm = m.copy()
    mm.update(i.encode("latin-1"))
    if mm.hexdigest().startswith("00000"):
        break

print(i)
