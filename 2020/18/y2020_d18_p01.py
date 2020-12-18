import fileinput as fi
import re

def eval_expr(e):
    e = e.split()
    l = int(e[0])
    for i in range(1,len(e),2):
        if e[i] == '+':
            l += int(e[i+1])
        else:
            l *= int(e[i+1])

    return l


ans = 0
for expr in map(str.rstrip, fi.input()):
    diff = 1
    while diff > 0:
        expr, diff = re.subn(r"\(([^()]+)\)", lambda x: str(eval_expr(x.group(1))), expr)

    ans += eval_expr(expr)

print(ans)
