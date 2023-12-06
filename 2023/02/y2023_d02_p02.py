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
        maxr = max(r["red"] for r in game)
        maxb = max(r["blue"] for r in game)
        maxg = max(r["green"] for r in game)

        ans += maxr*maxb*maxg
            
print(ans)
