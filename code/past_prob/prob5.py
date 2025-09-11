direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def block_move(g, x, y, dx, dy, added):
    nx = x + dx
    ny = y + dy
    num = g[x][y]
    while True:
        if g[nx][ny] == 0:
            nx += dx
            ny += dy
        elif g[nx][ny] != g[x][y] or (g[nx][ny] == g[x][y] and (nx, ny) in added):
            nx -= dx
            ny -= dy
            break
        else:
            added.add((nx, ny))
            num *= 2
            break
    g[x][y] = 0
    g[nx][ny] = num

def move(g, cnt):
    global res
    global n
    if cnt == 5:
        res = max(res, max(list(map(max, g))))
    else:
        for dx, dy in direct:
            new_g = [e[:] for e in g]
            added = set()
            if dy == 0:
                if dx == -1:
                    x = 1
                else:
                    x = n
                for cur_y in range(1, n + 1):
                    cur_x = x
                    for _ in range(n):
                        if new_g[cur_x][cur_y] != 0:
                            block_move(new_g, cur_x, cur_y, dx, dy, added)
                        cur_x -= dx
            else:
                if dy == -1:
                    y = 1
                else:
                    y = n
                for cur_x in range(1, n + 1):
                    cur_y = y
                    for _ in range(n):
                        if new_g[cur_x][cur_y] != 0:
                            block_move(new_g, cur_x, cur_y, dx, dy, added)
                        cur_y -= dy
            move(new_g, cnt + 1)

n = int(input())
graph = [[-1] * (n + 2)]
for _ in range(n):
    graph.append([-1] + list(map(int, input().split())) + [-1])
graph.append([-1] * (n + 2))
res = 0
move(graph, 0)
print(res)