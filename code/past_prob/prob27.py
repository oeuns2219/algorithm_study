direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
increase = [(1, 0), (0, 1)]
def move(b, a, num, di):
    global N
    global M
    x, y, size = a[num]
    dx, dy = direction[di]
    for n in range(size):
        for m in range(size):
            if b[x + n][y + m] == num:
                b[x + n][y + m] = 0

    nx = x + dx
    ny = y + dy
    if nx < 0:
        nx = N - size
    elif nx + size > N:
        nx = 0
    if ny < 0:
        ny = M - size
    elif ny + size > M:
        ny = 0
    a[num] = [nx, ny, size]
    ix, iy = increase[abs(dx)]
    for n in range(size):
        effect = []
        for m in range(size):
            l = b[nx + (n * dx) + (m * ix)][ny + (n * dy) + (m * iy)]
            if l != 0 and not l in effect:
                effect.append(l)
            b[nx + (n * dx) + (m * ix)][ny + (n * dy) + (m * iy)] = num
        for e in effect:
            move(b, a, e, di)

N, M, C = map(int, input().split())
board = []
commands = []
for _ in range(N):
    board.append(list(map(int, input().split())))
for _ in range(C):
    commands.append(list(map(int, input().split())))

A = max(map(max, board))
apps = [[-1, -1, 0] for _ in range(A + 1)]
detected = [False] * (A + 1)
prev = 0
for i in range(N):
    for j in range(M):
        k = board[i][j]
        if prev != 0 and prev != k:
            detected[prev] = True
            prev = 0
        if k != 0 and not detected[k]:
            if apps[k][2] == 0:
                apps[k] = [i, j, 1]
                prev = k
            else:
                apps[k][2] += 1

for command in commands:
    move(board, apps, command[0], command[1])
    for i in range(N):
        for j in range(M):
            print(board[i][j], end=' ')
        print('')
    print('')