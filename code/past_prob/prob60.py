from collections import deque

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(l, s):
    global N, direct
    visited = [[False] * N for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = True
    while q:
        cx, cy = q.popleft()
        for dx, dy in direct:
            nx, ny = cx + dx, cy + dy
            if N > nx >= 0 and N > ny >= 0 and l[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                for x, y in s[nx][ny]:
                    l[x][y] = 1

N, M = map(int, input().split())
lights = [[0] * N for _ in range(N)]
lights[0][0] = 1
switches = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    switches[a - 1][b - 1].append((c - 1, d - 1))
before = 1
after = 1
for a, b in switches[0][0]:
    lights[a][b] = 1
    after += 1
while before != after:
    before = after
    dfs(lights, switches)
    after = sum(map(sum, lights))
print(before)