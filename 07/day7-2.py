crabs = list(map(int,open("day7.txt","r").read().split(",")))
m = float("inf")
for i in range(max(crabs)):
    c = 0
    for cr in crabs:
        d = abs(cr-i)
        cr = (1+d)/2 * d
        c += cr
    m = min(c, m)
print(m)