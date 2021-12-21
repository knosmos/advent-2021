pos = [6,2]

def getRolls():
    r = []
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                r.append(i+j+k)
    return r

mem = {}

def rfn(pos, score, p):
    # Memoization
    a = (pos, score, p)
    if a in mem: return mem[a]

    wins = [0,0]
    for roll in getRolls():
        npos = list(pos)
        npos[p] += roll
        npos[p] = (npos[p]-1)%10+1
        npos = tuple(npos)
        
        nscore = list(score)
        nscore[p] += npos[p]
        nscore = tuple(nscore)
        
        # Check end condition
        if max(nscore) >= 21:
            wins[nscore.index(max(nscore))] += 1
        else:
            # Recurse
            i,j = rfn(npos, nscore, (p+1)%2)
            wins = [wins[0]+i, wins[1]+j]
    mem[a] = wins
    return wins
print(max(rfn(tuple(pos), (0,0), 0)))