import heapq
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
shortest_path = [INF] * (n + 1)
q = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

shortest_path[0] = 0
shortest_path[1] = 0
heapq.heappush(q, (0, 1))
while q:
    dist, cur = heapq.heappop(q)
    if shortest_path[cur] < dist:
        continue
    new_dist = dist + 1
    for k in graph[cur]:
        if new_dist < shortest_path[k]:
            shortest_path[k] = new_dist
            heapq.heappush(q, (new_dist, k))

max_min = max(shortest_path)
print(shortest_path.index(max_min), max_min, shortest_path.count(max_min))