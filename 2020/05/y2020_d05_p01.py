import fileinput

# Convert straight from pass to id
def pass_to_id(p):
    return sum(1<<(9-i) for (i,c) in enumerate(p) if c in "BR")
    
print(max(map(pass_to_id, fileinput.input())))
