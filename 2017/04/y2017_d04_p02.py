import fileinput as fi

ans = 0
for line in map(str.rstrip, fi.input()):
    seen = set()
    for word in line.split(" "):
        m = "".join(sorted(word))
        if m in seen:
            break
        else:
            seen.add(m)
    else:
        ans += 1

print(ans)
