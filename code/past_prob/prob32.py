from collections import deque

INF = int(1e9)
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(graph, visited, a, b):
    q = deque([[a, b, 0]])
    visited[a][b] = 0
    while q:
        ca, cb, cd = q.popleft()
        for da, db in direction:
            na = ca + da
            nb = cb + db
            nd = cd + 1
            if graph[na][nb] == 0 and visited[na][nb] > nd:
                visited[na][nb] = nd
                q.append([na, nb, nd])

N, M, F = map(int, input().split())
field = [[1] * (N + 2)]
for _ in range(N):
    field.append([1] + list(map(int, input().split())) + [1])
field.append([1] * (N + 2))
x, y = map(int, input().split())
guest = []
for _ in range(M):
    guest.append(list(map(int, input().split())))
fail = False
while guest and F:
    dist = [[INF] * (N + 2) for _ in range(N + 2)]
    gdist = []
    bfs(field, dist, x, y)
    for i in range(len(guest)):
        gx, gy, _, _ = guest[i]
        gdist.append((dist[gx][gy], gx, gy, i))
    gdist.sort()
    fuel, _, _, idx = gdist[0]
    F -= fuel
    cx, cy, nx, ny = guest.pop(idx)

    dist = [[INF] * (N + 2) for _ in range(N + 2)]
    bfs(field, dist, cx, cy)
    F -= dist[nx][ny]
    if F < 0:
        break
    F += 2 * dist[nx][ny]
    x, y = nx, ny
if F < 0:
    print(-1)
else:
    print(F)