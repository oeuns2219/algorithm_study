direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def blow(a, b, d, temp, g, vi):
    global R
    global C
    global direction
    g[a][b] += temp
    vi[a][b] = True
    if temp > 1:
        da, db = direction[d]
        al = [a + da, a + db, a - db]
        bl = [b + db, b + da, b - da]
        ca, cb = a + da, b + db
        if R > ca >= 0 and C > cb >= 0 and not is_wall(a, b, ca, cb) and not vi[ca][cb]:
            blow(ca, cb, d, temp - 1, g, vi)
        ba, bb = a + db, b + da
        ca, cb = ba + da, bb + db
        if R > ca >= 0 and C > cb >= 0 and not is_wall(a, b, ba, bb) and not is_wall(ba, bb, ca, cb) and not vi[ca][cb]:
            blow(ca, cb, d, temp - 1, g, vi)
        ba, bb = a - db, b - da
        ca, cb = ba + da, bb + db
        if R > ca >= 0 and C > cb >= 0 and not is_wall(a, b, ba, bb) and not is_wall(ba, bb, ca, cb) and not vi[ca][cb]:
            blow(ca, cb, d, temp - 1, g, vi)

def is_wall(a1, b1, a2, b2):
    global hor_wall
    global ver_wall
    if a1 == a2:
        a = a1
        b = min(b1, b2)
        return (a, b) in ver_wall
    else:
        a = max(a1, a2)
        b = b1
        return (a, b) in hor_wall

R, C, K = map(int, input().split())
heater = []
check = []
grid = [[0] * C for _ in range(R)]
cnt = 0
for x in range(R):
    row = list(map(int, input().split()))
    for y in range(C):
        if 5 > row[y] > 0:
            heater.append((x, y, row[y] - 1))
        elif row[y] == 5:
            check.append((x, y))
hor_wall = []
ver_wall = []
W = int(input())
for _ in range(W):
    x, y, t = map(int, input().split())
    if t == 0:
        hor_wall.append((x - 1, y - 1))
    else:
        ver_wall.append((x - 1, y - 1))

while True:
    for x, y, di in heater:
        dx, dy = direction[di]
        cx, cy = x + dx, y + dy
        visited = [[False] * C for _ in range(R)]
        blow(cx, cy, di, 5, grid, visited)

    change = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            x1, y1 = x - 1, y
            x2, y2 = x, y + 1
            if R > x1 >= 0 and C > y1 >= 0 and not (x, y) in hor_wall:
                value = abs(grid[x][y] - grid[x1][y1]) // 4
                if grid[x][y] > grid[x1][y1]:
                    change[x][y] -= value
                    change[x1][y1] += value
                else:
                    change[x][y] += value
                    change[x1][y1] -= value
            if R > x2 >= 0 and C > y2 >= 0 and not (x, y) in ver_wall:
                value = abs(grid[x][y] - grid[x2][y2]) // 4
                if grid[x][y] > grid[x2][y2]:
                    change[x][y] -= value
                    change[x2][y2] += value
                else:
                    change[x][y] += value
                    change[x2][y2] -= value
    grid = [[e1 + e2 for e1, e2 in zip(l1, l2)] for l1, l2 in zip(grid, change)]
    for i in range(R):
        if grid[i][0] > 0:
            grid[i][0] -= 1
        if grid[i][C - 1] > 0:
            grid[i][C - 1] -= 1
    for i in range(1, C - 1):
        if grid[0][i] > 0:
            grid[0][i] -= 1
        if grid[R - 1][i] > 0:
            grid[R - 1][i] -= 1
    cnt += 1
    if cnt == 101:
        break
    flag = True
    for x, y in check:
        if grid[x][y] < K:
            flag = False
            break
    if flag:
        break
print(cnt)