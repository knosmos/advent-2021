import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Day 1 Visualization")

with open("day1.txt","r") as fin:
    vals = list(map(int, fin.read().split("\n")))

rvals = [0]*100 + vals + [0]*100
fpsClock = pygame.time.Clock()
f = pygame.font.SysFont("Consolas",30)
f_large = pygame.font.SysFont("Consolas",200)
def render(i,c,r):
    screen.fill((22, 25, 37))

    # Get rolling average depth, for smooth depth transition
    avg_interval = vals[max(0,i-10):min(i+10,len(vals))]
    avg = sum(avg_interval)/len(avg_interval)
    
    # Draw depth map
    text = f_large.render(f"{vals[i]}m", 1, (40,40,60))
    screen.blit(text, (300-text.get_width()//2, 300-text.get_height()//2))
    scale = 1.5
    pygame.draw.circle(
        screen,
        (20, 189, 235),
        (300,int(vals[i]*scale+300-avg*scale)),
        10
    )
    pygame.draw.lines(
        screen, 
        (20, 189, 235),
        False,
        [(j*6, int(rvals[i+50+j]*scale+300-avg*scale)) for j in range(100)],
        5
    )
    
    # Draw indicators
    text = f.render("Direction: "+["↑","↓"][c], 1, (238, 66, 102))
    screen.blit(text, (10,10))
    text = f.render("Descents: "+str(r), 1, (238, 66, 102))
    screen.blit(text, (310,10))
    text = f.render("Sleigh Keys: Ocean Trench", 1, (238, 66, 102))
    screen.blit(text, (10,550))

    # Boilerplate
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    fpsClock.tick(30)

res = 0
for i in range(1, len(vals)):
    c = False
    if vals[i] + vals[i+1] + vals[i+2] > vals[i-1] + vals[i] + vals[i+1]:
        res += 1
        c = True
    render(i,c,res)
print(res)