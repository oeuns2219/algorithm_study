from collections import deque

direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def wall(k):
    walls =[False, False, False, False]
    while k != 0:
        if k >= 8:
            walls[0] = True
            k -= 8
        elif k >= 4:
            walls[1] = True
            k -= 4
        elif k >= 2:
            walls[2] = True
            k -= 2
        elif k >= 1:
            walls[3] = True
            k -= 1
    return walls

N, M = map(int, input().split())
castle = []
for _ in range(M):
    castle.append(list(map(int, input().split())))
is_wall = [list(map(wall, lst)) for lst in castle]

cnt = 0
max_size = 0
max_merge = 0
size_lst = []
visited = [[-1] * N for _ in range(M)]
for x in range(M):
    for y in range(N):
        if visited[x][y] == -1:
            size = 0
            visited[x][y] = cnt
            q = deque([[x, y]])
            while q:
                cx, cy = q.popleft()
                size += 1
                for i in range(4):
                    if not is_wall[cx][cy][i]:
                        dx, dy = direct[i]
                        nx, ny = cx + dx, cy + dy
                        if visited[nx][ny] == -1:
                            visited[nx][ny] = cnt
                            q.append([nx, ny])
            cnt += 1
            max_size = max(max_size, size)
            size_lst.append(size)

for x in range(M):
    for y in range(N):
        for i in range(4):
            if is_wall[x][y][i]:
                dx, dy = direct[i]
                nx, ny = x + dx, y + dy
                if M > nx >= 0 and N > ny >= 0 and visited[x][y] != visited[nx][ny]:
                    size = size_lst[visited[x][y]] + size_lst[visited[nx][ny]]
                    max_merge = max(max_merge, size)
print(cnt)
print(max_size)
print(max_merge)