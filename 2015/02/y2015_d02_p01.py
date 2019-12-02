import fileinput

ans = 0
for line in fileinput.input():
    l, w, h = [int(x) for x in line.strip().split("x")]
    ans += (2*l*w + 2*w*h + 2*h*l) + min(l*w, w*h, l*h)

print(ans)
