from collections import deque
import copy
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def gravity(graph):
    global N
    for x in range(N):
        for y in range(N):
            if graph[x][y] == -2:
                nx = x - 1
                while nx >= 0 and graph[nx][y] >= 0:
                    graph[nx + 1][y], graph[nx][y] = graph[nx][y], graph[nx + 1][y]
                    nx -= 1

def rotate_90(graph):
    global N
    new_graph = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            new_graph[N - y - 1][x] = graph[x][y]
    return new_graph

def bfs(graph, v, x, y):
    global N
    color = graph[x][y]
    v[x][y] = True
    vc = copy.deepcopy(v)
    size = 1
    num = 0
    q = deque([(x, y)])
    while q:
        cx, cy = q.popleft()
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not vc[nx][ny] and (graph[nx][ny] == color or graph[nx][ny] == 0):
                size += 1
                vc[nx][ny] = True
                if graph[nx][ny] != 0:
                    v[nx][ny] = True
                else:
                    num += 1
                q.append((nx, ny))
    return size, num

def clear(graph, pos):
    global N
    x, y = pos
    color = graph[x][y]
    graph[x][y] = -2
    q = deque([(x,y)])
    while q:
        cx, cy = q.popleft()
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and (graph[nx][ny] == color or graph[nx][ny] == 0):
                graph[nx][ny] = -2
                q.append((nx, ny))

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
score = 0
while True:
    max_size = 0
    max_num = 0
    max_pos = [0, 0]
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] > 0:
                s, n = bfs(grid, visited, i, j)
                if s > max_size:
                    max_size = s
                    max_num = n
                    max_pos[0] = i
                    max_pos[1] = j
                elif s == max_size:
                    if n >= max_num:
                        max_num = n
                        max_pos[0] = i
                        max_pos[1] = j
    if max_size < 2:
        break
    clear(grid, max_pos)
    score += max_size ** 2
    gravity(grid)
    grid = rotate_90(grid)
    gravity(grid)
print(score)