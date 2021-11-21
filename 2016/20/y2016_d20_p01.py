import fileinput as fi

ranges = []
for line in fi.input():
    a, b = line.split("-")
    ranges.append((int(a),int(b)))

ans = 0
for l, h in sorted(ranges):
    if ans < l:
        break
    else:
        ans = max(h+1, ans)

print(ans)
