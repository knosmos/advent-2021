from collections import deque

data = list(map(lambda i:list(map(int,i)),open("day15.txt","r").read().split("\n")))
newdata = [[0]*len(data)*5 for _ in range(len(data)*5)]
def wrap(k):
    return (k-1)%9+1

for i in range(len(newdata)):
    for j in range(len(newdata)):
        newdata[i][j] = wrap(data[i%len(data)][j%len(data[0])] + i//len(data) + j//len(data[0]))

data = newdata
dist = [[float("inf")]*len(data[0]) for _ in range(len(data))]
dist[0][0] = 0

q = deque([(0,0)])
while len(q) > 0:
    x,y = q.popleft()
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[0]):
            continue
        if dist[nx][ny] > dist[x][y] + data[nx][ny]:
            dist[nx][ny] = dist[x][y] + data[nx][ny]
            q.append((nx,ny))
print(dist[-1][-1])