from rich import print
data = [list(map(int,list(i))) for i in open("day9.txt","r").read().split("\n")]
print(data)
r = 0

for i in range(len(data)):
    for j in range(len(data[0])):
        n = [
            [i-1,j],
            [i,j-1],
            [i+1,j],
            [i,j+1]
        ]
        for k in n:
            if k[0] >= 0 and k[1] >= 0 and k[0] < len(data) and k[1] < len(data[0]):
                if data[k[0]][k[1]] <= data[i][j]:
                    break
        else:
           
print(r)