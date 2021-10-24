import fileinput as fi

INPUT = "".join(fi.input()).rstrip()

groups = INPUT.split("\n\n")
# print(groups[-1])
lines = list(INPUT.splitlines())


GLOBAL_MIN = 1000000000000000000000
# Round returns the mana cost of winning that turn.
# it is -1 if you loose
def combat(pHP, pMP, bHP, bAT, effects, pTurn, cost=0, depth=0):
    global GLOBAL_MIN

    if cost >= GLOBAL_MIN:
        # We are pruning because it's worse 
        return -1

    if pMP < 0:
        # print("cannot afford to call that spell")
        return -1

    pDEF = 0

    shield, poison, recharge = effects 

    if shield > 0:
        pDEF += 7
        shield -= 1
        
    if poison > 0:
        bHP -= 3
        poison -= 1

    if recharge > 0:
        pMP += 101
        recharge -= 1
    
    effects = (shield, poison, recharge)

    if bHP <= 0:
        if GLOBAL_MIN > cost:
            print("we are setting a new lower limit of", cost, depth)
            GLOBAL_MIN = cost
        # GLOBAL_MIN = min(GLOBAL_MIN, cost)
        return 0
   
    # This is a boss turn, since we want to early exit
    if not pTurn:
        pHP -= max(1, bAT - pDEF)
        if pHP <= 0:
            return -1
        else:
            return combat(pHP, pMP, bHP, bAT, effects, not pTurn, cost=cost, depth=depth+1)


    # Here we have a player turn

    min_use = None
   
    # Missile
    cost_missile = combat(pHP, pMP-53, bHP-4, bAT, effects, not pTurn, cost=cost+53, depth=depth+1)
    if cost_missile != -1:
        if min_use is None:
            min_use = 53 + cost_missile

        min_use = min(min_use, 53 + cost_missile)
    
    # Drain
    cost_drain = combat(pHP+2, pMP-73, bHP-2, bAT, effects, not pTurn, cost=cost+73, depth=depth+1)
    if cost_drain != -1:
        if min_use is None:
            min_use = 73 + cost_drain

        min_use = min(min_use, 73 + cost_drain)

    # Effects
    if effects[0] == 0:
        neffects = (effects[0] + 6, effects[1], effects[2])
        cost_shield = combat(pHP, pMP-113, bHP, bAT, neffects, not pTurn, cost=cost+113, depth=depth+1)
        if cost_shield != -1:
            if min_use is None:
                min_use = 113 + cost_shield

            min_use = min(min_use, 113 + cost_shield)



    if effects[1] == 0:
        neffects = (effects[0], effects[1] + 6, effects[2])
        cost_poison = combat(pHP, pMP-173, bHP, bAT, neffects, not pTurn, cost=cost+173, depth=depth+1)
        if cost_poison != -1:
            if min_use is None:
                min_use = 173 + cost_poison

            min_use = min(min_use, 173 + cost_poison)


    if effects[2] == 0:
        neffects = (effects[0], effects[1], effects[2]+5)
        cost_recharge = combat(pHP, pMP-229, bHP, bAT, neffects, not pTurn, cost=cost+229, depth=depth+1)
        if cost_recharge != -1:
            if min_use is None:
                min_use = 229 + cost_recharge

            min_use = min(min_use, 229 + cost_recharge)

    if min_use is None:
        return -1
    else:
        if depth < 5:
            print("we at depth {} with: {}".format(depth, min_use))
        return min_use



boss = (58, 9, 0)

print(combat(50, 500, 58, 9, (0, 0, 0), True) )
