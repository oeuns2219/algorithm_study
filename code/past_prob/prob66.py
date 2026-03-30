from collections import deque

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
island_di = direct + [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def find_island(g, a, b, k):
    global N, M, island_di
    max_a, max_b = 0, 0
    min_a, min_b = N, M
    q = deque([[a, b]])
    g[a][b] = str(k)
    while q:
        ca, cb = q.popleft()
        max_a, max_b = max(max_a, ca), max(max_b, cb)
        min_a, min_b = min(min_a, ca), min(min_b, cb)
        for da, db in island_di:
            na, nb = ca + da, cb + db
            if N > na >= 0 and M > nb >= 0 and g[na][nb] == 'x':
                g[na][nb] = str(k)
                q.append([na, nb])
    return max_a, max_b, min_a, min_b, a, b

def check(g, k, a, b):
    global N, M, direct
    visited = [[False] * M for _ in range(N)]
    q = deque([[a, b]])
    visited[a][b] = True
    while q:
        ca, cb = q.popleft()
        for da, db in direct:
            na, nb = ca + da, cb + db
            if N > na >= 0 and M > nb >= 0 and not visited[na][nb] and g[na][nb] != str(k):
                visited[na][nb] = True
                q.append([na, nb])
            elif not (N > na >= 0 and M > nb >= 0):
                return False
    return True

def propagate(h, c, k):
    for idx in range(len(c[k])):
        er = c[k][idx]
        h[er] = max(h[er], h[k] + 1)
        propagate(h, c, er)

N, M = map(int, input().split())
graph = []
island = []
for _ in range(N):
    graph.append(list(input()))

for x in range(N):
    for y in range(M):
        if graph[x][y] == 'x':
            n  = len(island)
            island.append(find_island(graph, x, y, n))
num = len(island)
height = [0] * num
contained = [[] for _ in range(num)]
for i in range(num - 1):
    for j in range(i + 1, num):
        max_ix, max_iy, min_ix, min_iy, ix, iy = island[i]
        max_jx, max_jy, min_jx, min_jy, jx, jy = island[j]
        if max_ix >= max_jx and min_ix <= min_jx and max_iy >= max_jy and min_iy <= min_jy:
            if check(graph, i, jx, jy):
                contained[j].append(i)
                propagate(height, contained, j)
        elif max_ix <= max_jx and min_ix >= min_jx and max_iy <= max_jy and min_iy >= min_jy:
            if check(graph, j, ix, iy):
                contained[i].append(j)
                propagate(height, contained, i)

if len(height) != 0:
    for i in range(max(height) + 1):
        print(height.count(i), end=' ')
else:
    print(-1, end=' ')