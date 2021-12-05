fin = open("day4.txt","r").read().split("\n\n")
order = list(map(int, fin[0].split(",")))
boards = []
for b in fin[1:]:
    boards.append(list(map(lambda i:list(map(int,i.split())),b.split("\n"))))

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

for num in order:
    nboards = []
    for board in boards:
        for row in range(5):
            for col in range(5):
                if board[row][col] == num:
                    board[row][col] = -1
        if not test(board):
            nboards.append(board)
    if len(boards) == 1 and test(boards[0]):
        s = 0
        for row in range(5):
            for col in range(5):
                if boards[0][row][col] != -1:
                    s += boards[0][row][col]
        print(s*num)
        break
    boards = nboards