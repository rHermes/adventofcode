import fileinput as fi
import re

def eval_expr(e):
    # Evaluate + first
    diff = 1
    while diff > 0:
        e, diff = re.subn(r"(\d+) \+ (\d+)", lambda x: str(int(x.group(1)) + int(x.group(2))), e)

    # Only multiply is left
    ans = 1
    for x in map(int,e.split()[::2]):
        ans *= x

    return ans


ans = 0
for expr in map(str.rstrip, fi.input()):
    # Expand paranthesis
    diff = 1
    while diff > 0:
        expr, diff = re.subn(r"\(([^()]+)\)", lambda x: str(eval_expr(x.group(1))), expr)

    ans += eval_expr(expr)

print(ans)
