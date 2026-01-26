from collections import deque

direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, K, R = map(int, input().split())
road_right = [[False] * N for _ in range(N)]
road_below = [[False] * N for _ in range(N)]
cows = []
graph = [[False] * N for _ in range(N)]

for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    if r1 == r2:
        r = r1
        c = min(c1, c2)
        road_right[r - 1][c - 1] = True
    else:
        r = min(r1, r2)
        c = c1
        road_below[r - 1][c - 1] = True
for _ in range(K):
    r, c = map(int, input().split())
    cows.append((r - 1, c - 1))
    graph[r - 1][c - 1] = True
visited = [[False] * N for _ in range(N)]
nums = []

for cow in cows:
    if not visited[cow[0]][cow[1]]:
        cnt = 1
        q = deque([(cow[0], cow[1])])
        visited[cow[0]][cow[1]] = True
        while q:
            cr, cc = q.popleft()
            for dr, dc in direct:
                nr, nc = cr + dr, cc + dc
                if cr == nr:
                    right = True
                else:
                    right = False
                r, c = min(cr, nr), min(cc, nc)
                if N > nr >= 0 and N > nc >= 0 and not ((right and road_right[r][c]) or (not right and road_below[r][c])) and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    if graph[nr][nc]:
                        cnt += 1
        nums.append(cnt)
res = 0
left = K
for num in nums:
    left -= num
    res += num * left
print(res)