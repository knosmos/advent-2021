import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,700))
pygame.display.set_caption("Day 25 Visualization")

from copy import deepcopy
state = [list(i) for i in open("day25.txt","r").read().split("\n")]
rows = len(state)
cols = len(state[0])
nstate = [["."]*cols for _ in range(rows)]
c = 0

clock = pygame.time.Clock()
f = pygame.font.Font(None,40)
def render(state):
    sy = 600/cols
    sx = 600/rows
    screen.fill((25, 21, 22))
    for y in range(rows):
        for x in range(cols):
            if state[y][x] == ">": pygame.draw.rect(screen, (217, 3, 104), (x*sx,y*sy,sx,sy))
            elif state[y][x] == "v": pygame.draw.rect(screen, (133, 203, 51), (x*sx,y*sy,sx,sy))
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
    screen.blit(f.render(f"step {c}",1,(249, 248, 248)),(10,610))
    clock.tick(20)
    pygame.display.flip()

while True:
    render(state)
    nstate = [["."]*cols for _ in range(rows)]
    for y in range(rows):
        for x in range(cols):
            if state[y][x] == ">":
                if state[y][(x+1)%cols] == ".":
                    nstate[y][(x+1)%cols] = ">"
                else:
                    nstate[y][x] = ">"
            if state[y][x] == "v": nstate[y][x] = "v"
    nstate1 = deepcopy(nstate)
    for y in range(rows):
        for x in range(cols):
            if state[y][x] == "v":
                if nstate1[(y+1)%rows][x] == ".":
                    nstate[(y+1)%rows][x] = "v"
                    nstate[y][x] = "."
                else:
                    nstate[y][x] = "v"
    c += 1
    if state == nstate:
        break
    state = nstate
    nstate = [["."]*cols for _ in range(rows)]

print(c)
while True:
    render(state)