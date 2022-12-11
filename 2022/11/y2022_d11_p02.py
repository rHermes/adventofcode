import fileinput as fi
import re
import math
import heapq

"""
Ok, so the task is solved like this:

We need to figure out a way to limit the numbers. The way we do this, is by
using modulus arithmetic. + and * are well defined under this property, so what is
left for us to do is to find the number M, to use as the modulus number.

We need M to be such that ((a % M) % N) == a % N for all a's.

The first observation here is that N <= M, in order for this to work. The only other
thing we need is that if a % M == 0, then a % N == 0. As long as these properties
hold, we can safely perform operations in (mod M) and be sure that the answers in
(mod N) will be the same.

The only way to fit these requirements is if M is a multiple of N. Since we have
multiple different (mod N), we need to find the least common multiple between all the
N's, as that number will fulfill the requirements set out above, for all monkeys.

You can read more about this stuff here:

https://en.wikipedia.org/wiki/Chinese_remainder_theorem

That theorem is about a different problem, but the idea is the same.

"""

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


def one_round(monkeys, inspects, M):
    for i in range(len(monkeys)):
       items, op, divt, true_monkey, false_monkey = monkeys[i]
       inspects[i] += len(items)
       for item in items:
           neww = op(item) % M

           if neww % divt == 0:
               monkeys[true_monkey][0].append(neww)
           else:
               monkeys[false_monkey][0].append(neww)

       monkeys[i][0].clear()

def solve(text):
    monkeys = parse_input(text)
    M = math.lcm(*[monkey[2] for monkey in monkeys])

    inspects = [0 for _ in monkeys]
    for _ in range(10000):
        one_round(monkeys, inspects, M)

    a, b = heapq.nlargest(2, inspects)
    return a * b


INPUT = "".join(fi.input()).rstrip()
print(solve(INPUT))
