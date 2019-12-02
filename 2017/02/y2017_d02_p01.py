import fileinput

sheet = [[int(x) for x in line.strip().split()] for line in fileinput.input()]
ans = sum([max(row) - min(row) for row in sheet])

print(ans)
