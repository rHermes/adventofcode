import fileinput as fi

games = []
for line in map(str.rstrip, fi.input()):
    id_part, po = line.split(": ")
    id = int(id_part.split(" ")[1])
    
    rounds_str = po.split("; ")
    rounds = []
    for round in rounds_str:
        items = round.split(", ")
        balls = {"blue": 0, "green": 0, "red": 0}
        for i in items:
            amount, color = i.split(" ")
            balls[color.strip()] += int(amount)
        
        rounds.append(balls)
    
    games.append((id, rounds))

ans = 0
for id, game in games:
    for r in game:
        if 12 < r["red"] or 13 < r["green"] or 14 < r["blue"]:
            break
    else:
        ans += id
            
print(ans)
