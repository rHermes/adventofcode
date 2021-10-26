import fileinput as fi
import re


GLOBAL_MIN = 1e100
def combat(pHP, pMP, bHP, bAT, effects, pTurn, cost=0):
    global GLOBAL_MIN

    if cost >= GLOBAL_MIN or pMP < 0:
        # We are pruning because it's worse or because we are dead
        return

    pDEF = 0

    shield, poison, recharge = effects

    if shield > 0: pDEF += 7
    if poison > 0: bHP -= 3
    if recharge > 0: pMP += 101

    effects = tuple([max(x-1, 0) for x in effects])

    # If we have a situation where the boss is dead we take it.
    if bHP <= 0:
        GLOBAL_MIN = min(GLOBAL_MIN, cost)
        return

    # This is a boss turn, since we want to early exit
    if not pTurn:
        pHP -= max(1, bAT - pDEF)
        if pHP > 0:
            combat(pHP, pMP, bHP, bAT, effects, not pTurn, cost=cost)

        return


    # Missile
    combat(pHP, pMP-53, bHP-4, bAT, effects, not pTurn, cost=cost+53)

    # Drain
    combat(pHP+2, pMP-73, bHP-2, bAT, effects, not pTurn, cost=cost+73)

    # shield
    if effects[0] == 0:
        neffects = (6, effects[1], effects[2])
        combat(pHP, pMP-113, bHP, bAT, neffects, not pTurn, cost=cost+113)

    # Posions
    if effects[1] == 0:
        neffects = (effects[0], 6, effects[2])
        cost_poison = combat(pHP, pMP-173, bHP, bAT, neffects, not pTurn, cost=cost+173)

    # Recharge
    if effects[2] == 0:
        neffects = (effects[0], effects[1], 5)
        cost_recharge = combat(pHP, pMP-229, bHP, bAT, neffects, not pTurn, cost=cost+229)



boss = list(map(int,re.findall("[1-9][0-9]*", "".join(fi.input()))))

combat(50, 500, boss[0], boss[1], (0, 0, 0), True)
print(GLOBAL_MIN)

