def bfs(graph, visited, city):
    queue = [city]
    while len(queue) != 0:
        cur_city = queue.pop(0)
        for new_city in graph[cur_city]:
            if visited[new_city] is None:
                visited[new_city] = visited[cur_city] + 1
                queue.append(new_city)


n, m, k, x = map(int, input().split())
nodes = [[] for _ in range(n)]
dists = [None] * n
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)

dists[x-1] = 0
bfs(nodes, dists, x-1)
cnt = dists.count(k)
if cnt == 0:
    print(-1)
else:
    for _ in range(cnt):
        idx = dists.index(k)
        print(idx+1)
        dists[idx] = None