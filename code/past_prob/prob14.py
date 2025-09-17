direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def watch(ng, nx, ny, dx, dy, cnt):
    global n
    global m
    while n > nx >= 0 and m > ny >= 0 and ng[nx][ny] != 6:
        if ng[nx][ny] == 0:
            ng[nx][ny] = 7
            cnt += 1
        nx += dx
        ny += dy
    return cnt

def check_site(g, c, cnt):
    global n
    global m
    global max_cnt
    if c:
        t, x, y = c.pop()
        if t == 1:
            for dx, dy in direct:
                ng = [e[:] for e in g]
                nx = x + dx
                ny = y + dy
                ncnt = watch(ng, nx, ny, dx, dy, cnt)
                check_site(ng, c, ncnt)
        elif t == 2:
            for k in range(2):
                ng = [e[:] for e in g]
                dx, dy = direct[k]
                nx = x + dx
                ny = y + dy
                ncnt = watch(ng, nx, ny, dx, dy, cnt)
                dx, dy = direct[k + 2]
                nx = x + dx
                ny = y + dy
                ncnt = watch(ng, nx, ny, dx, dy, ncnt)
                check_site(ng, c, ncnt)
        elif t == 3:
            for k in range(4):
                ng = [e[:] for e in g]
                dx, dy = direct[k]
                nx = x + dx
                ny = y + dy
                ncnt = watch(ng, nx, ny, dx, dy, cnt)
                dx, dy = direct[(k + 1) % 4]
                nx = x + dx
                ny = y + dy
                ncnt = watch(ng, nx, ny, dx, dy, ncnt)
                check_site(ng, c, ncnt)
        elif t == 4:
            for k in range(4):
                ng = [e[:] for e in g]
                dx, dy = direct[(k + 1) % 4]
                nx = x + dx
                ny = y + dy
                ncnt = watch(ng, nx, ny, dx, dy, cnt)
                dx, dy = direct[(k + 2) % 4]
                nx = x + dx
                ny = y + dy
                ncnt = watch(ng, nx, ny, dx, dy, ncnt)
                dx, dy = direct[(k + 3) % 4]
                nx = x + dx
                ny = y + dy
                ncnt = watch(ng, nx, ny, dx, dy, ncnt)
                check_site(ng, c, ncnt)
        else:
            for dx, dy in direct:
                nx = x + dx
                ny = y + dy
                cnt = watch(g, nx, ny, dx, dy, cnt)
            check_site(g, c, cnt)
        c.append((t, x, y))
    else:
        max_cnt = max(max_cnt, cnt)

n, m = map(int, input().split())
graph = []
cctv = []
total = 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if 5 >= row[j] >= 1:
            cctv.append((row[j], i, j))
        elif row[j] == 0:
            total += 1
    graph.append(row)
max_cnt = 0
check_site(graph, cctv, 0)
print(total - max_cnt)