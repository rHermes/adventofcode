import fileinput


G = {}
for line in fileinput.input():
    a, b = line.rstrip().split(")")
    G[b] = a


# your trip
your_trip = ["YOU"]
while (your_trip[-1] in G):
    your_trip.append(G[your_trip[-1]])

sant_trip = ["SAN"]
while (sant_trip[-1] in G):
    sant_trip.append(G[sant_trip[-1]])

for nod in your_trip:
    if nod in sant_trip:
        break


print(your_trip.index(nod) + sant_trip.index(nod) - 2)
