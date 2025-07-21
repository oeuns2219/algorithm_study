def dfs(g, v, s):
    for node in g[s]:
        if not v[node]:
            print(node + 1, end=' ')
            v[node] = True
            dfs(g, v, node)

n, m, k = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    graph[i] = list(set(graph[i]))
    graph[i].sort()

visited = [False] * n
visited[k-1] = True
print(k, end=' ')
dfs(graph, visited, k-1)

print('')

visited = [False] * n
visited[k-1] = True
print(k, end=' ')
queue = [k - 1]
while len(queue) != 0:
    cur = queue.pop(0)
    for l in graph[cur]:
        if not visited[l]:
            print(l + 1, end=' ')
            visited[l] = True
            queue.append(l)