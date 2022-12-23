import re
# import collections as cs
import math


# import typing


@tuple
class Blueprint():
    id: int
    ore_robot_ore_cost: int
    clay_robot_ore_cost: int
    ob_robot_ore_cost: int
    ob_robot_clay_cost: int
    geo_robot_ore_cost: int
    geo_robot_ob_cost: int

@tuple
class GameState:
    blueprint: Blueprint

    ore: int = 0
    clay: int = 0
    ob: int = 0

    # incoming_ore_robots: int = 0
    # incoming_clay_robots: int = 0
    # incoming_ob_robots: int = 0

    ore_robots: int = 1
    clay_robots: int = 0
    ob_robots: int = 0
    geo_robots: int = 0

    time : int = 0

    def sig(self) -> int:
        return hash((self.time, self.ore, self.clay, self.ob, self.ore_robots, self.clay_robots, self.ob_robots, self.geo_robots))


def get_blueprints(filename: str) -> List[Blueprint]:
    with open(filename) as f:
        blueprints: list[Blueprint] = []
        for line in f:
            id, a, b, c, d, e, h = list(map(int, re.findall("-?[0-9]+", line)))
            blueprints.append(Blueprint(id, a, b, c, d, e, h))
            
        return blueprints

TN = 32

# Returns the maximum number of geos you can get. We assume here that we can only build one
# robot each round.
def best_possible(cache: dict[int, int], state: GameState) -> int:
    if TN <= state.time:
        return 0

    if state.time == TN-1:
        return state.geo_robots


    sig = state.sig()
    if sig in cache:
        return cache[sig]


    # The minimum we can get is the geo_robots
    ans = (TN-state.time)*state.geo_robots


    # We but an ore robot
    if state.blueprint.ore_robot_ore_cost <= state.ore:
        next_turn = GameState(
                blueprint=state.blueprint,
                time=state.time+1,
                ore=state.ore + state.ore_robots - state.blueprint.ore_robot_ore_cost,
                clay=state.clay + state.clay_robots,
                ob=state.ob + state.ob_robots,
                ore_robots=state.ore_robots + 1,
                clay_robots=state.clay_robots,
                ob_robots=state.ob_robots,
                geo_robots=state.geo_robots,
                )

        ans = max(ans, state.geo_robots + best_possible(cache, next_turn))
    elif 0 < state.ore_robots:
        time_til_enough_ore = int(math.ceil((state.blueprint.ore_robot_ore_cost - state.ore) / state.ore_robots))
        time_spent = time_til_enough_ore + 1
        if time_spent + state.time <= TN:
            next_turn = GameState(
                    blueprint=state.blueprint,
                    time=state.time+time_spent,
                    ore=state.ore + state.ore_robots*time_spent - state.blueprint.ore_robot_ore_cost,
                    clay=state.clay + state.clay_robots*time_spent,
                    ob=state.ob + state.ob_robots*time_spent,
                    ore_robots=state.ore_robots + 1,
                    clay_robots=state.clay_robots,
                    ob_robots=state.ob_robots,
                    geo_robots=state.geo_robots,
                    )

            ans = max(ans, state.geo_robots*time_spent + best_possible(cache, next_turn))

    # We but an clay
    if state.blueprint.clay_robot_ore_cost <= state.ore:
        next_turn = GameState(
                blueprint=state.blueprint,
                time=state.time+1,
                ore=state.ore + state.ore_robots - state.blueprint.clay_robot_ore_cost,
                clay=state.clay + state.clay_robots,
                ob=state.ob + state.ob_robots,
                ore_robots=state.ore_robots,
                clay_robots=state.clay_robots + 1,
                ob_robots=state.ob_robots,
                geo_robots=state.geo_robots,
                )

        ans = max(ans, state.geo_robots + best_possible(cache, next_turn))
    elif 0 < state.ore_robots:
        time_til_enough_ore = int(math.ceil((state.blueprint.clay_robot_ore_cost - state.ore) / state.ore_robots))
        time_spent = time_til_enough_ore + 1
        if time_spent + state.time <= TN:
            next_turn = GameState(
                    blueprint=state.blueprint,
                    time=state.time+time_spent,
                    ore=state.ore + state.ore_robots*time_spent - state.blueprint.clay_robot_ore_cost,
                    clay=state.clay + state.clay_robots*time_spent,
                    ob=state.ob + state.ob_robots*time_spent,
                    ore_robots=state.ore_robots,
                    clay_robots=state.clay_robots + 1,
                    ob_robots=state.ob_robots,
                    geo_robots=state.geo_robots,
                    )

            ans = max(ans, state.geo_robots*time_spent + best_possible(cache, next_turn))

    # We but an ob robot
    if state.blueprint.ob_robot_ore_cost <= state.ore and state.blueprint.ob_robot_clay_cost <= state.clay:
        next_turn = GameState(
                blueprint=state.blueprint,
                time=state.time+1,
                ore=state.ore + state.ore_robots - state.blueprint.ob_robot_ore_cost,
                clay=state.clay + state.clay_robots - state.blueprint.ob_robot_clay_cost,
                ob=state.ob + state.ob_robots,
                ore_robots=state.ore_robots,
                clay_robots=state.clay_robots,
                ob_robots=state.ob_robots + 1,
                geo_robots=state.geo_robots,
                )

        ans = max(ans, state.geo_robots + best_possible(cache, next_turn))
    elif 0 < state.ore_robots and 0 < state.clay_robots:
        time_til_enough_ore = int(math.ceil((state.blueprint.ob_robot_ore_cost - state.ore) / state.ore_robots))
        time_til_enough_clay = int(math.ceil((state.blueprint.ob_robot_clay_cost - state.clay) / state.clay_robots))
        time_spent = max(time_til_enough_ore, time_til_enough_clay) + 1
        if time_spent + state.time <= TN:
            next_turn = GameState(
                    blueprint=state.blueprint,
                    time=state.time+time_spent,
                    ore=state.ore + state.ore_robots*time_spent - state.blueprint.ob_robot_ore_cost,
                    clay=state.clay + state.clay_robots*time_spent - state.blueprint.ob_robot_clay_cost,
                    ob=state.ob + state.ob_robots*time_spent,
                    ore_robots=state.ore_robots,
                    clay_robots=state.clay_robots,
                    ob_robots=state.ob_robots + 1,
                    geo_robots=state.geo_robots,
                    )

            ans = max(ans, state.geo_robots*time_spent + best_possible(cache, next_turn))

    # We but an geo robot
    if state.blueprint.geo_robot_ore_cost <= state.ore and state.blueprint.geo_robot_ob_cost <= state.ob:
        next_turn = GameState(
                blueprint=state.blueprint,
                time=state.time+1,
                ore=state.ore + state.ore_robots - state.blueprint.geo_robot_ore_cost,
                clay=state.clay + state.clay_robots,
                ob=state.ob + state.ob_robots - state.blueprint.geo_robot_ob_cost,
                ore_robots=state.ore_robots,
                clay_robots=state.clay_robots,
                ob_robots=state.ob_robots,
                geo_robots=state.geo_robots+1,
                )

        ans = max(ans, state.geo_robots + best_possible(cache, next_turn))
    elif 0 < state.ore_robots and 0 < state.ob_robots:
        time_til_enough_ore = int(math.ceil((state.blueprint.geo_robot_ore_cost - state.ore) / state.ore_robots))
        time_til_enough_ob = int(math.ceil((state.blueprint.geo_robot_ob_cost - state.ob) / state.ob_robots))
        time_spent = max(time_til_enough_ore, time_til_enough_ob) + 1
        if time_spent + state.time <= TN:
            next_turn = GameState(
                    blueprint=state.blueprint,
                    time=state.time+time_spent,
                    ore=state.ore + state.ore_robots*time_spent - state.blueprint.geo_robot_ore_cost,
                    clay=state.clay + state.clay_robots*time_spent,
                    ob=state.ob + state.ob_robots*time_spent - state.blueprint.geo_robot_ob_cost,
                    ore_robots=state.ore_robots,
                    clay_robots=state.clay_robots,
                    ob_robots=state.ob_robots,
                    geo_robots=state.geo_robots+1,
                    )

            ans = max(ans, state.geo_robots*time_spent + best_possible(cache, next_turn))



    cache[sig] = ans
    return ans



def calc_quality_level(blueprint: Blueprint) -> int:
    cache: dict[int, int] = {}
    state = GameState(blueprint = blueprint)
    score = best_possible(cache, state)

    print(blueprint.id, score)
    return score

ans = 0
# blueprints = get_blueprints("example.txt")
blueprints = get_blueprints("input.txt")

# 1 26 (Also with new version)

# 2 21
# 
# 3 13

# ! 1 28
# ans = 13 * 26
ans = 1
# @par
for blueprint in blueprints[:3]:
    score = calc_quality_level(blueprint)
    # ans += score
    ans *= score

print(ans)
