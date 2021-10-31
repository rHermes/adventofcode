import fileinput as fi
import hashlib


# Input parsing
INPUT = "".join(fi.input()).strip().encode('ascii')

ans = ""
for i in range(100000000000000):
    hsh = hashlib.md5(INPUT + str(i).encode("ascii")).hexdigest()

    if hsh.startswith("00000"):
        ans += hsh[5]
        if len(ans) == 8:
            break

print(ans)
