import fileinput as fi

ans = 0

for line in map(str.rstrip, fi.input()):
    digits = [x for x in line if x.isdigit()]
    ans += int(digits[0] + digits[-1])

print(ans)
