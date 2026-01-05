from collections import deque
import heapq
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(graph, visited, a, b):
    global R
    global C
    global direction
    visited[a][b] = True
    q = deque([[a, b]])
    cluster = []
    heapq.heappush(cluster, [-a, b])
    on_ground = False
    while q:
        ca, cb = q.popleft()
        if ca == R - 1:
            on_ground = True
        for da, db in direction:
            na, nb = ca + da, cb + db
            if R > na >= 0 and C > nb >= 0 and graph[na][nb] == 'x' and not visited[na][nb]:
                visited[na][nb] = True
                heapq.heappush(cluster, [-na, nb])
                q.append([na, nb])
    while not on_ground:
        new_cluster = []
        while cluster:
            ca, cb = heapq.heappop(cluster)
            graph[-ca][cb] = '.'
            graph[-ca + 1][cb] = 'x'
            heapq.heappush(new_cluster, [ca - 1, cb])
            if -ca + 1 == R - 1 or (not ([ca - 2, cb] in (cluster + new_cluster)) and graph[-ca + 2][cb] == 'x'):
                on_ground = True
        cluster = new_cluster


R, C = map(int, input().split())
cave = []
for _ in range(R):
    cave.append(list(input()))
N = int(input())
stick = list(map(int, input().split()))
from_left = True
for height in stick:
    x = R - height
    if from_left:
        from_left = False
        y = 0
        dy = 1
    else:
        from_left = True
        y = C - 1
        dy = -1

    while C > y >= 0:
        if cave[x][y] == 'x':
            cave[x][y] = '.'
            if C > y - 1 >= 0 and cave[x][y - 1] == 'x':
                v = [[False] * C for _ in range(R)]
                bfs(cave, v, x, y - 1)
            if R > x - 1 >= 0 and cave[x - 1][y] == 'x':
                v = [[False] * C for _ in range(R)]
                bfs(cave, v, x - 1, y)
            if C > y + 1 >= 0 and cave[x][y + 1] == 'x':
                v = [[False] * C for _ in range(R)]
                bfs(cave, v, x, y + 1)
            if R > x + 1 >= 0 and cave[x + 1][y] == 'x':
                v = [[False] * C for _ in range(R)]
                bfs(cave, v, x + 1, y)
            break
        else:
            y += dy

for s in cave:
    print(''.join(s))