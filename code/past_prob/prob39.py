direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diagonal = [(-1, -1), (-1, 1,), (1, 1), (1, -1)]

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
clouded = []
for _ in range(M):
    di, si = map(int, input().split())
    dx, dy = direction[di - 1]
    dx *= si
    dy *= si
    B = [[False] * N for _ in range(N)]
    while cloud:
        x, y = cloud.pop()
        nx, ny = (x + dx) % N, (y + dy) % N
        A[nx][ny] += 1
        B[nx][ny] = True
        clouded.append((nx, ny))
    while clouded:
        x, y = clouded.pop()
        cnt = 0
        for dx, dy in diagonal:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and N > ny >= 0 and A[nx][ny] > 0:
                cnt += 1
        A[x][y] += cnt
    for x in range(N):
        for y in range(N):
            if not B[x][y] and A[x][y] >= 2:
                cloud.append((x, y))
                A[x][y] -= 2

print(sum(map(sum, A)))