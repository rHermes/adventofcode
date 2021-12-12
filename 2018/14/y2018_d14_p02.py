def part1(n: int) -> str:
    w = [3, 7]
    a, b = 0, 1

    while len(w) < n+10:
        c = w[a] + w[b]
        digits = [int(x) for x in str(c)]
        w.extend(digits)
        a = (a + w[a] + 1) % len(w)
        b = (b + w[b] + 1) % len(w)

    lop = []
    for j in range(n,n+10):
        lop.append(str(w[j % len(w)]))

    return "".join(lop)

def part2(s: str) -> int:
    w = [3, 7]
    cur = "37"
    a, b = 0, 1
    i = 0
    while True:
        kw = cur.find(s, -10)
        if kw != -1:
            return kw

        c = w[a] + w[b]
        digits = [int(x) for x in str(c)]
        w.extend(digits)
        cur += str(c)
        a = (a + w[a] + 1) % len(w)
        b = (b + w[b] + 1) % len(w)


tc_1 = [
    (5, "0124515891"),
    (9,"5158916779"),
    (18, "9251071085"),
    (2018, "5941429882"),
    (652601, "1221283494"),
]
for i, o in tc_1:
    k = part1(i)
    if k != o:
        print("part1 of {} should yield {}, but gave {}".format(i, o, k))

tc_2 = [
    ("01245", 5),
    ("51589", 9),
    ("92510", 18),
    ("59414", 2018),
    ("652601", 20261485),
]
for ik, ok in tc_2:
    kk = part2(ik)
    if kk != ok:
        print("part2 of {} should yield {}, but gave {}".format(ik, ok, kk))

print(part2("652601"))
