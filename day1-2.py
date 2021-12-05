with open("day1.txt","r") as fin:
    vals = list(map(int, fin.read().split("\n")))
res = 0
for i in range(1, len(vals)-2):
    if vals[i] + vals[i+1] + vals[i+2] > vals[i-1] + vals[i] + vals[i+1]:
        res += 1 
print(res)