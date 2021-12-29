import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Day 4 Visualization")

fin = open("day4.txt","r").read().split("\n\n")
order = list(map(int, fin[0].split(",")))
boards = []
for b in fin[1:]:
    boards.append(list(map(lambda i:list(map(int,i.split())),b.split("\n"))))

fpsClock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas",10)
def render(boards, first, last):
    screen.fill((22, 25, 37))
    for x in range(10):
        for y in range(10):
            board = boards[x*10+y]
            for row in range(5):
                for col in range(5):
                    t = str(board[row][col])
                    if board[row][col] == -1:
                        t = "X"
                    if first == board:
                        color = (33, 209, 159)
                    elif last == board:
                        color = (238, 66, 102)
                    elif test(board):
                        if t == "X":
                            color = (142, 168, 195)
                        else:
                            color = (94, 111, 129)
                    elif t == "X":
                        color = (255, 231, 76)
                    else:
                        color = (120, 203, 225)
                    text = font.render(t,1,color)
                    screen.blit(text,(x*70+col*13,y*70+row*13))
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    fpsClock.tick(15)

def test(board):
    for row in range(5):
        for col in range(5):
            if board[row][col] != -1:
                break
        else:
            return True
    for col in range(5):
        for row in range(5):
            if board[row][col] != -1:
                break
        else:
            return True
    return False

filled = [0]*len(boards)
last_filled = 0
first = None
last = None
for num in order:
    nboards = []
    render(boards, first, last)
    for i, board in enumerate(boards):
        if not filled[i]:
            for row in range(5):
                for col in range(5):
                    if board[row][col] == num:
                        board[row][col] = -1
            if test(board):
                filled[i] = 1
                last_filled = i
                if not first:
                    first = board                        
        nboards.append(board)
    if filled.count(0) == 0:
        last = boards[last_filled]
    boards = nboards

while True:
    render(boards, first, last)