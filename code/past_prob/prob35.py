from collections import deque
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(g, v, x, y):
    global direction
    global N
    cur_size = 1
    v[x][y] = True
    q = deque([(x, y)])
    while q:
        cx, cy = q.popleft()
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 2 ** N > nx >= 0 and 2 ** N > ny >= 0 and g[nx][ny] > 0 and not v[nx][ny]:
                cur_size += 1
                v[nx][ny] = True
                q.append((nx, ny))
    return cur_size

def turn(g, x1, y1, sz):
    x2, y2 = x1, y1 + sz
    x3, y3 = x2 + sz, y2
    x4, y4 = x3, y3 - sz

    for i in range(sz):
        buf = g[x4 - i][y4]
        g[x4 - i][y4] = g[x3][y3 - i]
        g[x3][y3 - i] = g[x2 + i][y2]
        g[x2 + i][y2] = g[x1][y1 + i]
        g[x1][y1 + i] = buf

    if sz != 1:
        turn(g, x1 + 1, y1 + 1, sz - 2)

N, Q = map(int, input().split())
graph = []
for _ in range(2 ** N):
    graph.append(list(map(int, input().split())))
level = list(map(int, input().split()))

for L in level:
    num = 2 ** (N - L)
    size = 2 ** L
    if L != 0:
        for j in range(num):
            for k in range(num):
                turn(graph, j * size, k * size, size - 1)
    melt = []
    for a in range(2 ** N):
        for b in range(2 ** N):
            if graph[a][b] > 0:
                cnt = 0
                for da, db in direction:
                    na, nb = a + da, b + db
                    if 2 ** N > na >= 0 and 2 ** N > nb >= 0 and graph[na][nb] > 0:
                        cnt += 1
                if cnt < 3:
                    melt.append((a, b))
    for a, b in melt:
        graph[a][b] -= 1

max_size = 0
visited = [[False] * (2 ** N) for _ in range(2 ** N)]
for a in range(2 ** N):
    for b in range(2 ** N):
        if graph[a][b] > 0 and not visited[a][b]:
            max_size = max(max_size, bfs(graph, visited, a, b))

print(sum(map(sum, graph)))
print(max_size)