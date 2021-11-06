import fileinput as fi

# Returns the thing to find in the out group
def find(s):
    for i in range(len(s)-2):
        if s[i] != s[i+1] and s[i] == s[i+2] and s[i] != " " and s[i+1] != " ":
            yield s[i+1] + s[i] + s[i+1]


ans = 0
for line in map(str.rstrip, fi.input()):
    raw = line.replace("[", " ").replace("]", " ").split(" ")
    outs = " ".join(raw[::2])
    ins = " ".join(raw[1::2])

    if any(x in outs for x in find(ins)):
        ans += 1

print(ans)
