data = list(map(lambda i:list(map(int,i)),open("day15.txt","r").read().split("\n")))

dist = [[float("inf")]*len(data[0]) for _ in range(len(data))]
dist[0][0] = 0

# Dijkstra's algorithm
q = [(0,0)]
while len(q) > 0:
    x,y = q.pop(0)
    if (x, y) == (len(data)-1, len(data[0])-1):
        print(dist[x][y])
        break
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[0]):
            continue
        if dist[nx][ny] > dist[x][y] + data[nx][ny]:
            dist[nx][ny] = dist[x][y] + data[nx][ny]
            q.append((nx,ny))