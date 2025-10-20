def move(board, a, b, size, h):
    while True:
        if a == 5 or board[a + 1][b] != 0:
            break
        if size == 2 and h and board[a + 1][b + 1] != 0:
            break
        a += 1
    board[a][b] = 1
    if size == 2:
        if h:
            board[a][b + 1] = 1
        else:
            board[a - 1][b] = 1

def down(board, n):
    for i in range(n):
        board[n - i] = board[n - i - 1]
    board[0] = [0] * 4

def erase(board):
    global score
    for i in range(4):
        if sum(board[2 + i]) == 4:
            score += 1
            down(board, 2 + i)


N = int(input())
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]
score = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    horizontal = False
    if t == 1:
        s = 1
    else:
        s = 2
        if t == 2:
            horizontal = True
    move(green, 0, y, s, horizontal)
    move(blue, 0, x, s, not horizontal)
    erase(green)
    erase(blue)
    while sum(green[1]) != 0:
        down(green, 5)
    while sum(blue[1]) != 0:
        down(blue, 5)
print(score)
print(sum(map(sum, green)) + sum(map(sum, blue)))