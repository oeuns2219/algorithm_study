from collections import deque

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def min_neighbor(g, v, a, b, h):
    global N, M, direct
    min_h = 9
    q = deque([[a, b]])
    v[a][b] = True
    while q:
        ca, cb = q.popleft()
        for da, db in direct:
            na, nb = ca + da, cb + db
            if N > na >= 0 and M > nb >= 0 and g[na][nb] < h and not v[na][nb]:
                v[na][nb] = True
                q.append([na, nb])
            elif N > na >= 0 and M > nb >= 0 and g[na][nb] >= h:
                min_h = min(min_h, g[na][nb])
            elif not (N > na >= 0 and M > nb >= 0):
                min_h = 0
                break
        if min_h == 0: break
    return min_h

N, M = map(int, input().split())
pool = []
for _ in range(N):
    pool.append(list(map(int, input())))
before = sum(map(sum, pool))
already = [[False] * M for _ in range(N)]

for x in range(N):
    for y in range(M):
        if not already[x][y]:
            visited = [[False] * M for _ in range(N)]
            height = min_neighbor(pool, visited, x, y, pool[x][y] + 1)
            if height != 0:
                already = [[e3 or e4 for e3, e4 in zip(e1, e2)] for e1, e2 in zip(already, visited)]
                for i in range(N):
                    for j in range(M):
                        if visited[i][j]:
                            pool[i][j] = height
after = sum(map(sum, pool))
print(after - before)