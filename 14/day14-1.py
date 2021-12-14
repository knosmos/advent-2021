data = open("day14.txt","r").read().split("\n")
poly = data[0]
pat = {}
for i in range(len(poly)-1):
    k = poly[i]+poly[i+1]
    if k in pat:
        pat[k] += 1
    else:
        pat[k] = 1
r = {}
for i in data[2:]:
    a, b = i.split(" -> ")
    r[a] = b[0]

for i in range(10):
    n = {}
    for a, b in pat.items():
        ins = r[a]
        if not a[0]+ins in n:
            n[a[0]+ins] = 0
        if not ins+a[1] in n:
            n[ins+a[1]] = 0
        n[a[0]+ins] += b
        n[ins+a[1]] += b
    pat = n

ct1 = {}
ct2 = {}
for a, b in pat.items():
    if not a[0] in ct1: ct1[a[0]] = 0
    if not a[1] in ct2: ct2[a[1]] = 0
    ct1[a[0]] += b
    ct2[a[1]] += b
ct = {}
for k in ct1.keys():
    ct[k] = max(ct1[k], ct2[k])
print(max(ct.values())-min(ct.values()))