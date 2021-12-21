pos = [6,2]

def getRolls():
    r = []
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                r.append(i+j+k)
    return r

mem = {}

def rfn(pos1, pos2, score1, score2):
    # Memoization
    a = (pos1, pos2, score1, score2)
    if a in mem: return mem[a]
    
    for roll in getRolls():
        # Check end condition
        if max(score1, score2) >= 21:
            mem[a] = 

    # Recurse