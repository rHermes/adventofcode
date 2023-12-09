import fileinput as fi
import collections as cs

trans = { "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "T": 10, "J": 1, "Q": 12, "K": 13, "A": 14 }

hand_to_score = {
        (1, 1, 1, 1, 1): 1,
        (1, 1, 1, 2): 2,
        (1, 2, 2): 3,
        (1, 1, 3): 4,
        (2, 3): 5,
        (1, 4): 6,
        (5,): 7
}

scores = []
for line in map(str.rstrip, fi.input()):
    hand, bid = line.split(" ")
    counts = cs.Counter(hand)
    
    # replace the J with the second most use character
    if "J" in counts:
        spec = counts["J"]
        del counts["J"]
        if counts:
            w = counts.most_common(1)[0][0]
            counts[w] += spec
        else:
            counts["A"] = 5


    vals = tuple(sorted(counts.values()))
    score = hand_to_score[vals]
    nh = tuple(trans[c] for c in hand)
    scores.append((score, nh, int(bid)))


scores.sort()

print(sum(i * bid for i, (_, _, bid) in enumerate(scores, start=1)))
