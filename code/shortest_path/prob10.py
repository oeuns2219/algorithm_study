INF = int(1e9)

def DFS(g, n, vi, stack):
    global cycles

    for node, _ in g[n]:
        if not vi[node]:
            vi[node] = True
            DFS(g, node, vi, stack + [node])
        else:
            if node in stack:
                idx = stack.index(node)
                cycles.append((stack[idx], stack[-1]))

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
shortest_path = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    shortest_path[a][b] = c

for j in range(1, v + 1):
    shortest_path[j][j] = 0

for k in range(1, v + 1):
    for x in range(1, v + 1):
        for y in range(1, v + 1):
            shortest_path[x][y] = min(shortest_path[x][y], shortest_path[x][k] + shortest_path[k][y])

visited = [False] * (v + 1)
cycles = []
min_cycle_costs = INF
for i in range(1, v + 1):
    if not visited[i]:
        visited[i] = True
        DFS(graph, i, visited, [i])

if not cycles:
    print(-1)
else:
    for cycle in cycles:
        min_cycle_costs = min(min_cycle_costs, shortest_path[cycle[0]][cycle[1]] + shortest_path[cycle[1]][cycle[0]])
    print(min_cycle_costs)