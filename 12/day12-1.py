data=[i.split("-") for i in open("day12.txt").read().split("\n")]
verts = sorted(list(set([i[0] for i in data]+[i[1] for i in data])))
adj=[set() for i in range(len(verts))]
for i in data:
    adj[verts.index(i[0])].add(verts.index(i[1]))
    adj[verts.index(i[1])].add(verts.index(i[0]))
c = 0
def rfn(v,p=set()):
    global c
    print(p)
    if verts[v] == "end":
        c += 1
        return
    for n in adj[v]:
        if n not in p:
            if verts[v].islower():
                p = p.union({v})
            rfn(n,p)
rfn(verts.index("start"))
print(c)