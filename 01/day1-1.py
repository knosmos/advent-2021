with open("day1.txt","r") as fin:
    vals = list(map(int, fin.read().split("\n")))
res = 0
for i in range(1, len(vals)):
    if vals[i] > vals[i-1]:
        res += 1
print(res)