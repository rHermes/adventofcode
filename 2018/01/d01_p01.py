import fileinput

ans = 0
for line in fileinput.input():
    ans += int(line.rstrip())
print(ans)
