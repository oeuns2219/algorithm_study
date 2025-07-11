connected = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(visited, dist, start):
    global n
    global m
    global connected
    queue = [start]

    while len(queue) != 0:
        x, y = queue.pop(0)
        visited[x][y] = 0
        for direct in connected:
            new_x = x + direct[0]
            new_y = y + direct[1]
            if new_x >= 0 and new_y >= 0 and new_x < n and new_y < m and visited[new_x][new_y]:
                queue.append((new_x, new_y))
                dist[new_x][new_y] = dist[x][y] + 1
    print(dist)
    print(dist[n-1][m-1])

n, m = map(int, input().split())
graph = []
distant = [[0]*m for _ in range(n)]
distant[0][0] = 1
for _ in range(n):
    graph.append(list(map(int, input())))

bfs(graph, distant, (0, 0))