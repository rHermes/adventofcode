import collections
import fileinput as fi
import functools as ft
import re
import string


# This is based on the following:
# chr((ord(s) - ord("a") + n) % (ord("z") - ord("a") + 1) + ord("a"))
def smart_shift(s, n):
    return (ord(s) - 97 + n) % 26 + 97

@ft.cache
def create_trans(n):
   return {ord(a): smart_shift(a, n) for a in string.ascii_lowercase}


for line in fi.input():
    m  = re.match(r"(.*)-([0-9]+)\[(.*)\]", line)
    if not m:
        continue

    name, sid, ch = m.groups()

    c = collections.Counter(sorted(name.replace("-", "")))
    check = "".join(x for x, _ in c.most_common(5))

    if check != ch:
        continue

    shift = create_trans(int(sid) % len(string.ascii_lowercase))
    shift[ord("-")] = ord(" ")
    real = name.translate(shift)

    if "northpole" in real:
        print(sid)
