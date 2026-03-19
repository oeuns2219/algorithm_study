def find_way(r, d, t):
    global N
    global min_time
    if len(r) == N:
        min_time = min(min_time, t)
    else:
        for i in range(N):
            if not i in r:
                find_way(r + [i], d, t + d[r[-1]][i])

N, K = map(int, input().split())
dist = []
for _ in range(N):
    dist.append(list(map(int, input().split())))

for k in range(N):
    for a in range(N):
        for b in range(N):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

route = [K]
min_time = int(1e9)
find_way(route, dist, 0)
print(min_time)
