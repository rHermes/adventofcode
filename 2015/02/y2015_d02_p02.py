import fileinput

ans = 0
for line in fileinput.input():
    l, w, h = [int(x) for x in line.strip().split("x")]
    a, b, _ = sorted([l, w, h])
    ans += (a*2 + b*2) + (l*w*h)

print(ans)
