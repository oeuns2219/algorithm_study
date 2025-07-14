n, k = map(int, input().split())
queues = [[] for _ in range(k)]
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            queues[graph[i][j] - 1].append((i, j))
s, x, y = map(int, input().split())
for _ in range(s):
    for idx in range(k):
        queue = queues[idx].copy()
        queues[idx] = []
        for pos in queue:
            if pos[0] > 0 and graph[pos[0] - 1][pos[1]] == 0:
                graph[pos[0] - 1][pos[1]] = idx + 1
                queues[idx].append((pos[0] - 1, pos[1]))
            if pos[0] < n-1 and graph[pos[0] + 1][pos[1]] == 0:
                graph[pos[0] + 1][pos[1]] = idx + 1
                queues[idx].append((pos[0] + 1, pos[1]))
            if pos[1] > 0 and graph[pos[0]][pos[1] - 1] == 0:
                graph[pos[0]][pos[1] - 1] = idx + 1
                queues[idx].append((pos[0], pos[1] - 1))
            if pos[1] < n-1 and graph[pos[0]][pos[1] + 1] == 0:
                graph[pos[0]][pos[1] + 1] = idx + 1
                queues[idx].append((pos[0], pos[1] + 1))

print(graph[x-1][y-1])