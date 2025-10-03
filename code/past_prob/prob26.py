direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def move(ch, inf, pi, n, rev):
    global direction

    x, y, di = pi[n]
    dx, dy = direction[di]
    nx = x + dx
    ny = y + dy
    if ch[nx][ny] == 0 or ch[nx][ny] == 1:
        idx = inf[x][y].index(k)
        moving = inf[x][y][idx:]
        inf[x][y] = inf[x][y][:idx]
        if ch[nx][ny] == 1:
            moving.reverse()
        inf[nx][ny] += moving
        for e in moving:
            pi[e][0] = nx
            pi[e][1] = ny
        if len(inf[nx][ny]) >= 4:
            return True
        else:
            return False
    else:
        if not rev:
            if di % 2 == 0:
                di += 1
            else:
                di -= 1
            pi[n][2] = di
            return move(ch, inf, pi, n, True)
        else:
            return False

N, K = map(int, input().split())
chess = [[2] * (N + 2)]
inform = [[[] for _ in range(N + 2)] for _ in range(N + 2)]
piece = []
for _ in range(N):
    row = [2] + list(map(int, input().split())) + [2]
    chess.append(row)
chess.append([2] * (N + 2))
for k in range(K):
    i, j, d = map(int, input().split())
    piece.append([i, j, d - 1])
    inform[i][j].append(k)

turn = 0
flag = False
while turn <= 1000 and not flag:
    for k in range(K):
        if move(chess, inform, piece, k, False):
            flag = True
            break
    turn += 1
if turn > 1000:
    print(-1)
else:
    print(turn)