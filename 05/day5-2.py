with open("day5.txt","r") as fin:
    pairs = list(map(lambda i:list(map(lambda j:list(map(int,j.split(","))),i.split(" -> "))), fin.read().split("\n")))
matrix = [[0]*1000 for _ in range(1000)]
for pair in pairs:
    if pair[0][0] == pair[1][0]:
        a = min(pair[0][1], pair[1][1])
        b = max(pair[0][1], pair[1][1])
        for i in range(a, b+1):
            matrix[i][pair[0][0]] += 1
    elif pair[0][1] == pair[1][1]:
        a = min(pair[0][0], pair[1][0])
        b = max(pair[0][0], pair[1][0])
        for i in range(a, b+1):
            matrix[pair[0][1]][i] += 1
    else:
        a1 = min(pair[0][0], pair[1][0])
        a2 = max(pair[0][0], pair[1][0])
        b1 = min(pair[0][1], pair[1][1])
        b2 = min(pair[0][1], pair[1][1])
        if pair[0][0] < pair[1][0]:
            a1 = pair[0][0]
            b1 = pair[0][1]
            a2 = pair[1][0]
            b2 = pair[1][1]
        else:
            a2 = pair[0][0]
            b2 = pair[0][1]
            a1 = pair[1][0]
            b1 = pair[1][1]
        if b1 > b2:
            m = -1
        else:
            m = 1
        for x in range(a1,a2+1):
            matrix[(x-a1)*m+b1][x] += 1

s = 0
for r in matrix:
    for c in r:
        if c >= 2:
            s += 1
#print(matrix)
print(s)