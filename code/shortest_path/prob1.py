INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x, k = map(int, input().split())

for i in range(1, n + 1):
    graph[i][i] = 0

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(b + 1, n + 1):
            stopover = graph[b][a] + graph[a][c]
            if graph[b][c] > stopover:
                graph[b][c] = stopover
                graph[c][b] = stopover

if graph[1][k] != INF and graph[k][x] != INF:
    print(graph[1][k] + graph[k][x])
else:
    print(-1)