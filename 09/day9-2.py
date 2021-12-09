data = [list(map(int,list(i))) for i in open("day9.txt","r").read().split("\n")]

def floodfill(i,j,v=set()):
    v.add((i,j))
    r = 1
    n = [
        [i-1,j],
        [i,j-1],
        [i+1,j],
        [i,j+1]
    ]
    for k in n:
        if k[0] >= 0 and k[1] >= 0 and k[0] < len(data) and k[1] < len(data[0]):
            if data[k[0]][k[1]] != 9 and not (k[0],k[1]) in v:
                r += floodfill(k[0], k[1], v)
    return r

b = []
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
            b.append(floodfill(i,j))
b.sort(reverse=True)
print(b[0]*b[1]*b[2])