import pygame, time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Day 11 Visualization")

fpsClock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas",50)
def render():
    global r, m, data
    screen.fill((22, 25, 37))
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != 0:
                color = (233//10*data[i][j],79//10*data[i][j],55//10*data[i][j])
            else:
                color = (220, 247, 99)
            screen.blit(font.render(str(data[i][j]), 1, color),(j*60+10, i*60+10))
    for e in pygame.event.get():
        if e.type == QUIT: pygame.quit()
    pygame.display.flip()
    fpsClock.tick(15)

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
    render()
    r += 1
print(r)
while True:
    render()