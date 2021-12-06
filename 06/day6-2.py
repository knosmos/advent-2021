fin = open("day6.txt","r").read()
fish = list(map(int,fin.split(",")))
fish.sort()

k = [fish.count(i) for i in range(9)]
for it in range(256):
    j = k.pop(0)
    k.append(j)
    k[6] += j
print(sum(k))
