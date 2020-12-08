import fileinput as fi

def solve(a, T=2020):
    for i, x in enumerate(a):
        s = set()
        for y in a[i+1:]:
            z = T - y - x
            if y in s:
                return x * y * z

            s.add(z)

print(solve([int(x) for x in fi.input()]))
