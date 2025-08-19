INF = int(1e9)

n = int(input())
m = int(input())
res = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    res[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    res[a][b] = min(res[a][b], c)

for k in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            res[x][y] = min(res[x][y], res[x][k] + res[k][y])

for d in range(1, n + 1):
    for e in range(1, n + 1):
        if res[d][e] == INF:
            print('0', end=' ')
        else:
            print(res[d][e], end=' ')
    print('')