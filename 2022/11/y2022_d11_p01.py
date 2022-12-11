import fileinput as fi
import re
import heapq

regex = (r"Monkey (\d+):\n"
	r"  Starting items: ((?:\d+, )*\d+)\n"
	r"  Operation: new = (.+)\n"
	r"  Test: divisible by (\d+)\n"
	r"    If true: throw to monkey (\d+)\n"
	r"    If false: throw to monkey (\d+)")


def parse_input(txt):
    groups = txt.split("\n\n")
    monkeys = []
    for (id, start_items, op, divt, tmonkey, fmonkey) in re.findall(regex, txt):
        id, divt, tmonkey, fmonkey = map(int, (id, divt, tmonkey, fmonkey))
        start_items = [int(x) for x in start_items.split(", ")]
        monkeys.append((start_items, eval("lambda old: " + op), divt, tmonkey, fmonkey))

    return monkeys


def one_round(monkeys, inspects):
    for i in range(len(monkeys)):
       items, op, divt, true_monkey, false_monkey = monkeys[i]
       inspects[i] += len(items)
       for item in items:
           neww = op(item) // 3
           if neww % divt == 0:
               monkeys[true_monkey][0].append(neww)
           else:
               monkeys[false_monkey][0].append(neww)

       monkeys[i][0].clear()

def solve(text):
    monkeys = parse_input(text)

    inspects = [0 for _ in monkeys]
    for _ in range(20):
        one_round(monkeys, inspects)

    a, b = heapq.nlargest(2, inspects)
    return a * b


INPUT = "".join(fi.input()).rstrip()
print(solve(INPUT))
