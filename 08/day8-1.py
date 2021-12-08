fin = open("day8.txt","r").read().split("\n")
for i in range(len(fin)):
    fin[i] = fin[i].split(" | ")[1]
output = [i.split() for i in fin]
print(output)
c = 0
for i in output:
    for j in i:
        if len(j) in [2, 3, 4, 7]:
            c += 1
print(c)