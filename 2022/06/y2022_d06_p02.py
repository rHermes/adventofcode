import fileinput as fi
import more_itertools as mit

N = 14
ans = N - 1
line = next(fi.input()).rstrip()
for kv in mit.windowed(line, N):
    ans += 1
    if len(set(kv)) == N:
        break

print(ans)
