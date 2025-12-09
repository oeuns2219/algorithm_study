from collections import deque
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dice_roll(dc, di):
    if di == 0:
        dc['up'], dc['east'], dc['down'], dc['west'] = dc['west'], dc['up'], dc['east'], dc['down']
    elif di == 1:
        dc['up'], dc['south'], dc['down'], dc['north'] = dc['north'], dc['up'], dc['south'], dc['down']
    elif di == 2:
        dc['up'], dc['east'], dc['down'], dc['west'] = dc['east'], dc['down'], dc['west'], dc['up']
    else:
        dc['up'], dc['south'], dc['down'], dc['north'] = dc['south'], dc['down'], dc['north'], dc['up']

def bfs(g, v, a, b):
    global direction
    global N
    global M
    q = deque([(a, b)])
    v[a][b] = True
    cnt = 1
    while q:
        ca, cb = q.popleft()
        for da, db in direction:
            na, nb = ca + da, cb + db
            if N > na >= 0 and M > nb >= 0 and g[ca][cb] == g[na][nb] and not v[na][nb]:
                v[na][nb] = True
                cnt += 1
                q.append((na, nb))
    return cnt

N, M, K = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

dice = dict()
dice['up'] = 1
dice['down'] = 6
dice['north'] = 2
dice['south'] = 5
dice['east'] = 3
dice['west'] = 4

direct = 0
score = 0
x = 0
y = 0
for _ in range(K):
    dx, dy = direction[direct]
    nx, ny = x + dx, y + dy
    if not (N > nx >= 0 and M > ny >= 0):
        direct = (direct + 2) % 4
        dx, dy = direction[direct]
        nx, ny = x + dx, y + dy
    x, y = nx, ny
    dice_roll(dice, direct)
    B = grid[x][y]
    visited = [[False] * M for _ in range(N)]
    C = bfs(grid, visited, x, y)
    score += B * C
    if dice['down'] > grid[x][y]:
        direct = (direct + 1) % 4
    elif dice['down'] < grid[x][y]:
        direct = (direct - 1) % 4
print(score)