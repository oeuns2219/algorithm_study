
INF = int(1e9)

N = int(input())
M = int(input())
floyd = []
for _ in range(N):
    floyd.append(list(map(int, input().split())))

for a in range(N):
    for b in range(N):
        if floyd[a][b] == 0 and a != b:
            floyd[a][b] = INF

for k in range(N):
    for a in range(N):
        for b in range(N):
            floyd[a][b] = min(floyd[a][b], floyd[a][k] + floyd[k][b])

route = list(map(int, input().split()))
res = True
for i in range(M - 1):
    if floyd[route[i] - 1][route[i + 1] - 1] == INF:
        res = False
        break
if res: print('YES')
else: print('NO')