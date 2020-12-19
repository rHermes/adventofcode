import fileinput as fi

from lark import Lark, LarkError

def parse_rules(rules, part='a'):
    if part == 'b':
        rules = rules.replace("8: 42", "8: 42 | 42 8")
        rules = rules.replace('11: 42 31', '11: 42 31 | 42 11 31')

    rules = rules.translate(str.maketrans("0123456789", 'abcdefghij'))
    parser = Lark(rules.strip(), start='a')

    return parser


INS = "".join(fi.input())
rules, messages = INS.split("\n\n")

p1 = parse_rules(rules)
p2 = parse_rules(rules,part='b')

ans_1 = 0
ans_2 = 0
for line in messages.splitlines():
    try:
        p2.parse(line)
        ans_2 += 1
        p1.parse(line)
        ans_1 += 1
    except LarkError:
        pass

print("Part 1: {}".format(ans_1))
print("Part 2: {}".format(ans_2))
