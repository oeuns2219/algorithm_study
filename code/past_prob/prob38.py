INF = int(1e9)
direction = [(0, 1), (1, 0)]

def adjust(g):
    global N
    add_g = [[0] * N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if g[a][b] != 0:
                for da, db in direction:
                    na, nb = a + da, b + db
                    if N > na >= 0 and N > nb >= 0 and g[na][nb] != 0:
                        d = abs(g[a][b] - g[na][nb]) // 5
                        if d > 0:
                            if g[a][b] > g[na][nb]:
                                add_g[a][b] -= d
                                add_g[na][nb] += d
                            else:
                                add_g[a][b] += d
                                add_g[na][nb] -= d
    new_g = [[c + d for c, d in zip(a, b)] for a, b in zip(g, add_g)]
    return new_g

def straighten(g, ll):
    global N
    a, b = ll
    na, nb = N - 1, 0
    for k in range(N):
        g[na][nb + k], g[a][b] = g[a][b], g[na][nb + k]
        a -= 1
        if g[a][b] == 0:
            b += 1
            a = N - 1

N, K = map(int, input().split())
graph = [[0] * N for _ in range(N - 1)]
graph.append(list(map(int, input().split())))
T = 0
while max(graph[N - 1]) - min(graph[N - 1]) > K:
    T += 1
    min_num = min(graph[N - 1])
    for n in range(N):
        if graph[N - 1][n] == min_num:
            graph[N - 1][n] += 1
    graph[N - 1][0], graph[N - 2][1] = graph[N - 2][1], graph[N - 1][0]
    x = N - 1
    y = N - 1
    flag = False
    left_low = [N - 1, 0]
    ground_len = 0
    height = 0
    while True:
        if not flag:
            if graph[x - 1][y] == 0:
                ground_len += 1
                y -= 1
            else:
                cx, cy = x, y
                nx, ny = x - 1, y + 1
                flag = True
                while graph[x][y] != 0:
                    height += 1
                    x -= 1
                if height > ground_len:
                    break
                else:
                    left_low[0] = cx
                    left_low[1] = cy + 1
        else:
            if graph[cx][cy] != 0:
                for i in range(height):
                    graph[cx - i][cy], graph[nx][ny + i] = graph[nx][ny + i], graph[cx - i][cy]
                cy -= 1
                nx -= 1
            else:
                flag = False
                x = N - 1
                y = N - 1
                ground_len = 0
                height = 0
    graph = adjust(graph)
    straighten(graph, left_low)
    left_low[0] = N - 1
    left_low[1] = (3 * (N // 4))
    cx, cy = N - 1, (N // 2) - 1
    nx, ny = N - 2, (N // 2)
    for i in range(N // 2):
        graph[cx][cy - i], graph[nx][ny + i] = graph[nx][ny + i], graph[cx][cy - i]
    cx, cy = N - 2, (3 * (N // 4)) - 1
    nx, ny = N - 3, (3 * (N // 4))
    for j in range(2):
        for i in range(N // 4):
            graph[cx + j][cy - i], graph[nx - j][ny + i] = graph[nx - j][ny + i], graph[cx + j][cy - i]
    graph = adjust(graph)
    straighten(graph, left_low)
print(T)