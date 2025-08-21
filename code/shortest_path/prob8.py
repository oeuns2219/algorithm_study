import heapq
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
shortest_path = [INF] * (v + 1)
q = []
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

shortest_path[k] = 0
heapq.heappush(q, (0, k))

while q:
    cost, vertex = heapq.heappop(q)
    if shortest_path[vertex] < cost:
        continue

    for new_vertex in graph[vertex]:
        new_cost = cost + new_vertex[1]
        if new_cost < shortest_path[new_vertex[0]]:
            shortest_path[new_vertex[0]] = new_cost
            heapq.heappush(q, (new_cost, new_vertex[0]))

for i in range(1, v + 1):
    if shortest_path[i] == INF:
        print('INF')
    else:
        print(shortest_path[i])