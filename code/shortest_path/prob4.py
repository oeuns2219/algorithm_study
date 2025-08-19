INF = int(1e9)

n, m = map(int, input().split())
gt_graph = [[INF] * (n + 1) for _ in range(n + 1)]
lt_graph = [[INF] * (n + 1) for _ in range(n + 1)]
for l in range(1, n + 1):
    gt_graph[l][l] = 0
    lt_graph[l][l] = 0

for _ in range(m):
    x, y = map(int, input().split())
    gt_graph[x][y] = 1
    lt_graph[y][x] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            gt_graph[i][j] = min(gt_graph[i][j], gt_graph[i][k] + gt_graph[k][j])
            lt_graph[i][j] = min(lt_graph[i][j], lt_graph[i][k] + lt_graph[k][j])

cnt = 0
all = set(range(1, n + 1))
for a in range(1, n + 1):
    comparable = set()
    for b in range(1, n + 1):
        if gt_graph[a][b] != INF or lt_graph[a][b] != INF:
            comparable.add(b)
    if comparable == all:
        cnt += 1
print(cnt)