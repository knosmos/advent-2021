data=[i.split("-") for i in open("day12.txt").read().split("\n")]
verts = sorted(list(set([i[0] for i in data]+[i[1] for i in data])))
adj=[set() for i in range(len(verts))]
for i in data:
    adj[verts.index(i[0])].add(verts.index(i[1]))
    adj[verts.index(i[1])].add(verts.index(i[0]))
c = 0
paths=set()
def rfn(v,p=set(),used=False,path=[]):
    global c
    if verts[v] == "end":
        if not tuple(path) in paths:
            c += 1
            paths.add(tuple(path))
        return
    for n in adj[v]:
        if n not in p and verts[n] != "start":
            if verts[v].islower():
                if not used:
                    rfn(n,p,True,path+[v])
                    rfn(n,p.union({v}),False,path+[v])
                else:
                    rfn(n,p.union({v}),True,path+[v])
            else:
                rfn(n,p,used,path+[v])
rfn(verts.index("start"))
print(c)