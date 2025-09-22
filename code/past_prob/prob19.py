direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(g, v, x, y):
    global N
    global L
    global R
    v[x][y] = True
    q = [(x, y)]
    u = []
    total = 0
    while q:
        cx, cy = q.pop(0)
        u.append((cx, cy))
        total += g[cx][cy]
        for dx, dy in direction:
            nx = cx + dx
            ny = cy + dy
            if N > nx >= 0 and N > ny >= 0 and not v[nx][ny] and R >= abs(g[cx][cy] - g[nx][ny]) >= L:
                v[nx][ny] = True
                q.append((nx, ny))
    population = total // len(u)
    for x, y in u:
        g[x][y] = population
    if len(u) == 1:
        return False
    else:
        return True

N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
change = False
day = 0
while True:
    visited = [[False] * N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if not visited[a][b]:
                change |= bfs(graph, visited, a, b)
    if change:
        day += 1
        change = False
    else:
        break
print(day)