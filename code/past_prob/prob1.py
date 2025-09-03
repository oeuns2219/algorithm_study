import heapq

direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def bfs(g, v, px, py):
    global shark_size
    global shark_exp
    q = []
    heapq.heappush(q, (0, px, py))
    v[px][py] = True
    while q:
        time, x, y = heapq.heappop(q)
        if g[x][y] < shark_size and g[x][y] != 0:
            g[x][y] = 0
            shark_exp += 1
            if shark_exp == shark_size:
                shark_size += 1
                shark_exp = 0
            return time, x, y
        for dx, dy in direct:
            if n > x + dx >= 0 and n > y + dy >= 0 and not v[x + dx][y + dy]:
                v[x + dx][y + dy] = True
                if g[x + dx][y + dy] <= shark_size:
                    heapq.heappush(q, (time + 1, x + dx, y + dy))
    return 0, 0, 0

n = int(input())
graph = []
shark_pos = []
shark_size = 2
shark_exp = 0
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 9:
            shark_pos.append(i)
            shark_pos.append(j)
            break

total = 0
x = shark_pos[0]
y = shark_pos[1]
graph[x][y] = 0
while True:
    visited = [[False] * n for _ in range(n)]
    time, x, y = bfs(graph, visited, x, y)
    if time == 0:
        break
    total += time
print(total)