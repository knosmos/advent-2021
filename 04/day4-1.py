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

end = False
for num in order:
    if end:
        break
    for board in boards:
        for row in range(5):
            for col in range(5):
                if board[row][col] == num:
                    board[row][col] = -1
        if test(board):
            s = 0
            for row in range(5):
                for col in range(5):
                    if board[row][col] != -1:
                        s += board[row][col]
            print(s*num)
            end = True
            break