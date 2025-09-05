direct = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
import copy
def direct_plus(di):
    if di == 8:
        return 1
    else:
        return di + 1

def find_position(g, fnum):
    for i in range(4):
        for j in range(4):
            if g[i][j][0] == fnum:
                return i, j
    return None
def fish_move(g):
    global direct
    for i in range(1, 17):
        pos = find_position(g, i)
        if not(pos is None):
            x, y = pos
            fish = g[x][y][0]
            di = g[x][y][1]
            dx, dy = direct[di]
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_x > 3 or new_y < 0 or new_y > 3 or g[new_x][new_y][0] == 17:
                di = direct_plus(di)
                while di != g[x][y][1]:
                    dx, dy = direct[di]
                    new_x = x + dx
                    new_y = y + dy
                    if new_x < 0 or new_x > 3 or new_y < 0 or new_y > 3 or g[new_x][new_y][0] == 17:
                        di = direct_plus(di)
                    else:
                        break
            if new_x < 0 or new_x > 3 or new_y < 0 or new_y > 3 or g[new_x][new_y][0] == 17:
                continue
            else:
                g[x][y][1] = di
                g[x][y], g[new_x][new_y] = g[new_x][new_y], g[x][y]

def possible_position(g, sp, di):
    global direct
    dx, dy = direct[di]
    x = sp[0] + dx
    y = sp[1] + dy
    plst = []
    while 4 > x >= 0 and 4 > y >= 0:
        if g[x][y][0] != 0:
            plst.append([x, y])
        x += dx
        y += dy
    return plst

def shark_move(g, sp, se):
    global direct
    global max_shark_eat
    fish_move(g)
    di = g[sp[0]][sp[1]][1]
    g[sp[0]][sp[1]][0] = 0
    plst = possible_position(g, sp, di)
    if len(plst) == 0:
        max_shark_eat = max(max_shark_eat, se)
    else:
        for p in plst:
            gc = copy.deepcopy(g)
            fish = gc[p[0]][p[1]][0]
            gc[p[0]][p[1]][0] = 17
            shark_move(gc, p, se + fish)

graph = []
for _ in range(4):
    an, ad, bn, bd, cn, cd, dn, dd = map(int, input().split())
    graph.append([[an, ad], [bn, bd], [cn, cd], [dn, dd]])
shark_pos = [0, 0]
shark_eat = graph[0][0][0]
max_shark_eat = 0
graph[0][0][0] = 17
shark_move(graph, shark_pos, shark_eat)
print(max_shark_eat)
