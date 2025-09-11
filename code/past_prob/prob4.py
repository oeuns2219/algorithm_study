import copy
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def new_int(e):
    if e == '#':
        return -1
    elif e == '.':
        return 0
    elif e == 'R':
        return 1
    elif e == 'B':
        return 2
    elif e == 'O':
        return 3
    else:
        return 4

def ball_move(g, rx, ry, bx, by, cnt):
    global res
    global n
    global m
    #for a in range(n):
        #for b in range(m):
            #print(g[a][b], end=' ')
        #print('')
    #print('')
    for dx, dy in direct:
        new_g = copy.deepcopy(g)
        new_rx = rx + dx
        new_ry = ry + dy
        before_blue = False
        end = False
        impossible = False
        while True:
            if new_g[new_rx][new_ry] == -1:
                new_rx -= dx
                new_ry -= dy
                break
            elif new_g[new_rx][new_ry] == 2:
                before_blue = True
                break
            elif new_g[new_rx][new_ry] == 3:
                end = True
                break
            else:
                new_rx += dx
                new_ry += dy
        if not before_blue:
            if end:
                new_g[rx][ry] = 0
            else:
                new_g[rx][ry] = 0
                new_g[new_rx][new_ry] = 1
        new_bx = bx + dx
        new_by = by + dy
        while True:
            if new_g[new_bx][new_by] == -1 or new_g[new_bx][new_by] == 1:
                new_bx -= dx
                new_by -= dy
                break
            elif g[new_bx][new_by] == 3:
                impossible = True
                break
            else:
                new_bx += dx
                new_by += dy
        if impossible:
            continue
        if end:
            res = min(res, cnt + 1)
            continue
        new_g[bx][by] = 0
        new_g[new_bx][new_by] = 2
        if before_blue:
            new_rx = new_bx - dx
            new_ry = new_by - dy
            new_g[rx][ry] = 0
            new_g[new_rx][new_ry] = 1
        if rx == new_rx and ry == new_ry and bx == new_bx and by == new_by:
            continue
        if cnt == 9:
            continue
        ball_move(new_g, new_rx, new_ry, new_bx, new_by, cnt + 1)

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(new_int, input())))
res = 11
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            r_x = i
            r_y = j
        elif graph[i][j] == 2:
            b_x = i
            b_y = j
ball_move(graph, r_x, r_y, b_x, b_y, 0)
if res > 10:
    print(-1)
else:
    print(res)