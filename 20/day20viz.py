# Uses Conway's Game of Life algorithm to make it more interesting
# Trims the image down to a certain size to preserve performance;
# this means that image will be inaccurate

import pygame, copy
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,650))
pygame.display.set_caption("Day 20 Visualization")

lines = open("sample.txt","r").read().split("\n")
alg = lines[0]
data = lines[2:]

clock = pygame.time.Clock()
f = pygame.font.SysFont("Consolas",20)
def render(data,i):
    rows = len(data)
    cols = len(data[0])
    sx = 600/cols
    sy = 600/rows
    screen.fill((25, 21, 22))
    for y in range(rows):
        for x in range(cols):
            if data[y][x] == "#":
                pygame.draw.rect(screen, (249, 248, 248), (x*sx,y*sy,sx,sy))
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
    screen.blit(f.render(f"enhancement {i}",1,(249, 248, 248)),(20,610))
    clock.tick(20)
    pygame.display.flip()

def enhance(data):
    n = len(data)
    l = len(data[0])
    # Pad outer ring of data with .s
    data = ["."*(n+20) for _ in range(10)] + ["."*10+i+"."*10 for i in data] + ["."*(n+20) for _ in range(10)]
    # ENHANCE
    output = []
    for i in range(1,len(data)-1):
        line = []
        for j in range(1,len(data)-1):
            square = [
                data[i-1][j-1],
                data[i-1][j],
                data[i-1][j+1],

                data[i][j-1],
                data[i][j],
                data[i][j+1],

                data[i+1][j-1],
                data[i+1][j],
                data[i+1][j+1]
            ]
            num = "".join(["0" if k == "." else "1" for k in square])
            #print(num)
            num = int(num,2)
            #print(num)
            out = alg[num]
            line.append(out)
        output.append("".join(line))
    return output

roi_size = 150
for i in range(500):
    data = enhance(data)
    data = data[8:-8]
    data = [i[8:-8] for i in data]
    if len(data[0]) > roi_size:
        data = data[(len(data)-roi_size)//2:-(len(data)-roi_size)//2]
        data = [k[(len(data[0])-roi_size)//2:-(len(data[0])-roi_size)//2] for k in data]
    render(data,i)