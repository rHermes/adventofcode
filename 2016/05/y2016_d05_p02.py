import fileinput as fi
import hashlib


# Input parsing
INPUT = "".join(fi.input()).strip().encode('ascii')

ans = ['' for _ in range(8)]
added = 0
for i in range(100000000000000):
    hsh = hashlib.md5(INPUT + str(i).encode("ascii")).hexdigest()

    if hsh.startswith("00000"):
        if not hsh[5].isnumeric() or int(hsh[5]) >= 8 or ans[int(hsh[5])] != "":
            continue

        ans[int(hsh[5])] = hsh[6]
        added += 1

        if added == 8:
            break

print("".join(ans))
