import pygame, textwrap, time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("Day 10 Visualization")

font = pygame.font.SysFont("Consolas",30)
fpsClock = pygame.time.Clock()
def render(current,stack,message=None):
    screen.fill((25, 21, 22))
    tx, ty = 20,-15
    wraplen = 30
    wrapper = textwrap.TextWrapper(width=wraplen)
    for i in wrapper.wrap(text=current):
        ty += 35
        screen.blit(font.render(i, 1, (255, 255, 255)), (tx, ty))
    stack_display = "".join([{"{":"}","[":"]","(":")","<":">"}[j] for j in stack[::-1]])
    for i in wrapper.wrap(text=stack_display):
        ty += 35
        screen.blit(font.render(i, 1, (100,100,100)), (tx, ty))
    if message:
        ty += 35
        screen.blit(font.render(message, 1, (41, 120, 160)), (tx, ty))
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
    pygame.display.flip()
    if message: time.sleep(1)
    fpsClock.tick(20)

data=open("day10.txt","r").read().split("\n")
res = []
for line in data:
    stack = []
    for i, char in enumerate(line):
        if char in "{[(<":
            stack.append(char)
        else:
            if {"{":"}","[":"]","(":")","<":">"}[stack[-1]] != char:
                render(line[:i+1],stack,"corrupt")
                break
            else:
                stack.pop()
        render(line[:i+1],stack)
    else:
        render(line,stack,"incomplete")
        completion = stack[::-1]
        r = 0
        for i in completion:
            r *= 5
            r += {"(":1,"[":2,"{":3,"<":4}[i]
        res.append(r)
res = sorted(res)[len(res)//2]
print(res)