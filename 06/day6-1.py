fish = list(map(int,open("day6.txt","r").read().split(",")))
for day in range(100):
    nfish = []
    for i in fish:
        i -= 1
        if i <= -1:
            nfish.append(8) 
            nfish.append(6)
        else:
            nfish.append(i)
    fish = nfish
print(len(fish))