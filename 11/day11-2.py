data=[list(map(int,list(i))) for i in open("day11.txt").read().split("\n")]
r = 0
m = [[0]*len(data[0]) for _ in range(len(data))]
def flash(y,x):
    global r, m, data
    m[y][x] = 1
    data[y][x] = 0
    for a in range(y-1,y+2):
        for b in range(x-1,x+2):
            if a!=y or b !=x:
                if a >= 0 and b >= 0 and a < len(data) and b < len(data[0]):
                    data[a][b] += 1
                    if data[a][b] > 9 and m[a][b] == 0:
                        flash(a,b)
def k():
    for i in data:
        for j in i:
            if j != 0:
                return True
    return False
while k():
    m = [[0]*len(data[0]) for _ in range(len(data))]
    for y in range(len(data)):
        for x in range(len(data[0])):
            data[y][x] += 1
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] > 9 and m[y][x] == 0:
                flash(y,x)
    for y in range(len(data)):
        for x in range(len(data[0])):
            if m[y][x] == 1:
                data[y][x] = 0
    r += 1
print(r)