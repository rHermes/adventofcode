import fileinput as fi

ans = 0
for line in map(str.rstrip, fi.input()):
    _, r = line.split(" | ")
    for word in r.split():
        if len(word) not in [5, 6]:
            ans += 1

print(ans)
