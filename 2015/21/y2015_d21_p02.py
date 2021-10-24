import fileinput as fi
import re

shop_text = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
""".lstrip()


def parse_group(g):
    ll = g.splitlines()
    items = []
    for l in ll[1:]:
        prts = l.split()
        cost, damage, armor = int(prts[-3]), int(prts[-2]), int(prts[-1])
        items.append((cost, damage, armor))

    return items

def combat(player, boss):
    pHP, pATK, pDEF = player
    bHP, bATK, bDEF = boss

    pTurn = True
    while bHP >0 and pHP > 0:
        if pTurn:
            bHP -= max(1, pATK - bDEF)
        else:
            pHP -= max(1, bATK - pDEF)

        pTurn = not pTurn

    return bHP <= 0


grps = shop_text.split("\n\n")
weps = parse_group(grps[0])
arms = parse_group(grps[1])
rings = parse_group(grps[2])

boss = list(map(int,re.findall("[1-9][0-9]*", "".join(fi.input()))))

max_cost = -1
for wep in weps:
    for arm in [None] + arms:
        for ring1 in [None] + rings:
            for ring2 in [None] + rings:
                if ring1 == ring2:
                    continue

                gear = []
                gear.append(wep)
                if arm:
                    gear.append(arm)
                if ring1:
                    gear.append(ring1)
                if ring2:
                    gear.append(ring2)

                cost, ATK, DEF = 0, 0, 0
                for c, a, d in gear:
                    cost += c
                    ATK += a
                    DEF += d

                if cost <= max_cost:
                    continue

                if not combat((100, ATK, DEF), boss):
                    max_cost = cost

print(max_cost)
