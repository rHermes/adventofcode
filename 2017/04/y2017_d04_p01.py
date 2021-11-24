import fileinput as fi

ans = 0
for line in map(str.rstrip, fi.input()):
    seen = set()
    for word in line.split(" "):
        if word in seen:
            break
        else:
            seen.add(word)
    else:
        ans += 1

print(ans)
