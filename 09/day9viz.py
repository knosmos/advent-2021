import pygame, time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Day 9 Visualization")
data = [list(map(int,list(i))) for i in open("day9.txt","r").read().split("\n")]
pygame.display.flip()
pygame.mouse.set_visible(False)

def floodfill(i,j,v=set()):
    v.add((i,j))
    render(v)
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

fpsClock = pygame.time.Clock()
def render(v):
    global data
    screen.fill((0,0,0))
    for i in range(len(data)):
        for j in range(len(data[0])):
            if not((i,j) in v):
                color = (int(255/10*data[i][j]),int(166/10*data[i][j]),int(43/10*data[i][j]))
            else:
                color = (int(2/10*data[i][j]),int(169/10*data[i][j]),int(234/10*data[i][j]))
            if (i,j) in l:
                color = (255,255,255)
            pygame.draw.rect(screen,color,(j*6,i*6,6,6))
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()

b = []
l = set()
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
            l.add((i,j))
            b.append(floodfill(i,j))
time.sleep(5)
b.sort(reverse=True)
print(b[0]*b[1]*b[2])