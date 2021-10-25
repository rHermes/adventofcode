import fileinput as fi
import hashlib


INPUT = "".join(fi.input()).rstrip()

groups = INPUT.split("\n\n")
# print(groups[-1])
lines = list(INPUT.splitlines())

for line in lines:
    key = line

i = 1
while True:
    tkey = key + str(i)
    m = hashlib.md5(tkey.encode("latin-1")).hexdigest()
    if m.startswith("000000"):
        break

    i += 1

print(i)


