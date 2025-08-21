import heapq
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
min_cost = [INF] * (n + 1)
shortest_path = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

q = []
min_cost[start] = 0
shortest_path[start] = [start]
heapq.heappush(q, (0, start))

while q:
    cost, city = heapq.heappop(q)
    if min_cost[city] < cost:
        continue

    for new_city in graph[city]:
        new_cost = cost + new_city[1]
        if min_cost[new_city[0]] > new_cost:
            min_cost[new_city[0]] = new_cost
            shortest_path[new_city[0]] = shortest_path[city] + [new_city[0]]
            heapq.heappush(q, (new_cost, new_city[0]))

print(min_cost[end])
print(len(shortest_path[end]))
for e in shortest_path[end]:
    print(e, end=' ')