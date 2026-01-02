direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def move(c, p, cp):
    global direction
    global K
    global max_len
    for j in range(K):
        a, b, di = p[j]
        if cp[a][b][0] == j:
            da, db = direction[di]
            na, nb = a + da, b + db
            if c[na][nb] == 0 or c[na][nb] == 1:
                for k in cp[a][b]:
                    p[k][0] = na
                    p[k][1] = nb
                if c[na][nb] == 0:
                    cp[na][nb] += cp[a][b]
                else:
                    cp[a][b].reverse()
                    cp[na][nb] += cp[a][b]
                cp[a][b] = []
                max_len = max(max_len, len(cp[na][nb]))
            else:
                if di % 2 == 0:
                    di += 1
                else:
                    di -= 1
                p[j][2] = di
                da, db = direction[di]
                na, nb = a + da, b + db
                if c[na][nb] == 0 or c[na][nb] == 1:
                    for k in cp[a][b]:
                        p[k][0] = na
                        p[k][1] = nb
                    if c[na][nb] == 0:
                        cp[na][nb] += cp[a][b]
                    else:
                        cp[a][b].reverse()
                        cp[na][nb] += cp[a][b]
                    cp[a][b] = []
                    max_len = max(max_len, len(cp[na][nb]))

N, K = map(int, input().split())
chess = [[2] * (N + 2)]
for _ in range(N):
    chess.append([2] + list(map(int, input().split())) + [2])
chess.append([2] * (N + 2))
piece = []
c_p = [[[] for _ in range(N + 2)] for _ in range(N + 2)]
for i in range(K):
    x, y, d = map(int, input().split())
    piece.append([x, y, d - 1])
    c_p[x][y].append(i)

max_len = 1
cnt = 0
while max_len < 4:
    cnt += 1
    if cnt > 1000:
        cnt = -1
        break
    move(chess, piece, c_p)
print(cnt)