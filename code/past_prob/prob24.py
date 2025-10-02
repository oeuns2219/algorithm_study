direction = [(-1, 0), (0, 1), (0, -1), (1, 0)]

def bfs(g, v, a, b, p, n):
    global direction
    global N
    q = []
    p[n - 1] += g[a][b]
    v[a][b] = n
    q.append((a, b))
    while q:
        a, b = q.pop(0)
        for da, db in direction:
            na = a + da
            nb = b + db
            if 0 <= na < N and 0 <= nb < N and v[na][nb] == 0:
                p[n - 1] += g[na][nb]
                v[na][nb] = n
                q.append((na, nb))

def draw_line(g, v, a, b, di, p, n):
    global direction
    global N
    da, db = direction[di]
    na = a + da
    nb = b + db
    while 0 <= na < N and 0 <= nb < N:
        v[na][nb] = n
        p[n - 1] += g[na][nb]
        na += da
        nb += db

N = int(input())
A = []
res = int(1e9)
for _ in range(N):
    A.append(list(map(int, input().split())))
for x in range(1, N - 1):
    for y in range(2, N):
        for d in range(2, N - x + 1):
            for d1 in range(1, d):
                d2 = d - d1
                if d1 <= y - 1 and d2 <= N - y:
                    population = [0] * 5
                    visited = [[0] * N for _ in range(N)]
                    population[4] += A[x - 1][y - 1]
                    visited[x - 1][y - 1] = 5
                    for diff in range(1, d1 + 1):
                        r1 = x + diff
                        c1 = y - diff
                        r2 = x + d2 + diff
                        c2 = y + d2 - diff
                        population[4] += A[r1 - 1][c1 - 1]
                        population[4] += A[r2 - 1][c2 - 1]
                        visited[r1 - 1][c1 - 1] = 5
                        visited[r2 - 1][c2 - 1] = 5
                    for diff in range(1, d2 + 1):
                        r1 = x + diff
                        c1 = y + diff
                        r2 = x + d1 + diff
                        c2 = y - d1 + diff
                        population[4] += A[r1 - 1][c1 - 1]
                        population[4] += A[r2 - 1][c2 - 1]
                        visited[r1 - 1][c1 - 1] = 5
                        visited[r2 - 1][c2 - 1] = 5
                    population[4] -= A[x + d1 + d2 - 1][y - d1 + d2 - 1]
                    draw_line(A, visited, x - 1, y - 1, 0, population, 1)
                    draw_line(A, visited, x + d2 - 1, y + d2 - 1, 1, population, 2)
                    draw_line(A, visited, x + d1 - 1, y - d1 - 1, 2, population, 3)
                    draw_line(A, visited, x + d1 + d2 - 1, y - d1 + d2 - 1, 3, population, 4)
                    bfs(A, visited, 0, 0, population, 1)
                    bfs(A, visited, 0, N - 1, population, 2)
                    bfs(A, visited, N - 1, 0, population, 3)
                    bfs(A, visited, N - 1, N - 1, population, 4)
                    for r in range(1, N + 1):
                        for c in range(1, N + 1):
                            if visited[r - 1][c - 1] == 0:
                                population[4] += A[r - 1][c - 1]
                                visited[r - 1][c - 1] = 5
                    if sum(map(sum, A)) != sum(population):
                        print('error')
                    res = min(res, max(population) - min(population))
print(res)