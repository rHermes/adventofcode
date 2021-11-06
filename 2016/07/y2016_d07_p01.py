import fileinput as fi

def abbas(s):
    for i in range(len(s)-3):
        if s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2]:
            return True

    return False


ans = 0
for line in map(str.rstrip, fi.input()):
    raw = line.replace("[", " ").replace("]", " ").split(" ")
    outs = raw[::2]
    ins = raw[1::2]

    if any(map(abbas, outs)) and not any(map(abbas, ins)):
        ans += 1


print(ans)
