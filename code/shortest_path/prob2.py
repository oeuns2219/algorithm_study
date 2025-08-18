import heapq
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
spath = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
q = []
spath[c] = 0
heapq.heappush(q, (0, c))
while q:
    dist, city = heapq.heappop(q)
    if spath[city] < dist:
        continue
    for i in graph[city]:
        if spath[i[0]] > dist + i[1]:
            spath[i[0]] = dist + i[1]
            heapq.heappush(q, (spath[i[0]], i[0]))

real_spath = [e for e in spath if e != INF]
print(n - spath.count(INF), max(real_spath))