pos = [6,2]
p = 0
sc = [0,0]
d = 1
n = 0
while True:
    for i in range(3):
        pos[p] += d
        pos[p] = (pos[p]-1)%10+1
        d = d%100+1
        n += 1
    sc[p] += pos[p]
    if max(sc) >= 1000:
        print(min(sc)*n)
        break
    p = not p