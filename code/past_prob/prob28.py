from collections import deque

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def rotate(g, num, di, ki):
    if di == 0:
        g[num] = g[num][-ki:] + g[num][:-ki]
    else:
        g[num] = g[num][ki:] + g[num][:ki]

def bfs(g, x, y):
    global N
    global M
    ori = g[x][y]
    g[x][y] = 0
    q = deque([[x, y]])
    while q:
        cx, cy = q.popleft()
        for dx, dy in direction:
            nx = cx + dx
            ny = cy + dy
            if ny < 0:
                ny = M - 1
            elif ny >= M:
                ny = 0

            if N + 1 > nx >= 0 and g[nx][ny] == ori:
                g[nx][ny] = 0
                q.append([nx, ny])

N, M, T = map(int, input().split())
graph = [[0] * M]
for _ in range(N):
    graph.append(list(map(int, input().split())))
for _ in range(T):
    x, d, k = map(int, input().split())
    n = 1
    while x * n <= N:
        rotate(graph, x * n, d, k)
        n += 1
    exist = False
    do = False
    cnt = 0
    for i in range(1, N + 1):
        for j in range(M):
            if graph[i][j] != 0:
                cnt += 1
                for di, dj in direction:
                    ni = i + di
                    nj = j + dj
                    if nj < 0:
                        nj = M - 1
                    elif nj >= M:
                        nj = 0

                    if N + 1 > ni >= 0 and graph[ni][nj] == graph[i][j]:
                        exist = True
                        do = True
                        break
                if do:
                    bfs(graph, i, j)
                    do = False
    if not exist and cnt != 0:
        aver = sum(map(sum, graph)) / cnt
        for i in range(1, N + 1):
            for j in range(M):
                if graph[i][j] != 0:
                    if graph[i][j] > aver:
                        graph[i][j] -= 1
                    elif graph[i][j] < aver:
                        graph[i][j] += 1
print(sum(map(sum, graph)))