crabs = list(map(int,open("day7.txt","r").read().split(",")))
m = float("inf")
for i in range(max(crabs)):
    c = 0
    for cr in crabs:
        c += abs(cr-i)
    m = min(c, m)
print(m)