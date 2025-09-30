direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def di_mp(di, flag):
    if flag:
        return (di + 1) % 4
    else:
        if di == 0:
            return 3
        else:
            return di - 1

def expand(x, y, g, ng):
    global direction
    global R
    global C
    origin = g[x][y]
    expansion = origin // 5
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if R > nx >= 0 and C > ny >= 0 and g[nx][ny] != -1:
            ng[nx][ny] += expansion
            origin -= expansion
    ng[x][y] += origin

def circulation(idx, g, flag):
    global direction
    global R
    global C
    x = idx
    y = 1
    di = 1
    dx, dy = direction[di]
    buf = 0
    while not(x == idx and y == 0):
        buf, g[x][y] = g[x][y], buf
        nx = x + dx
        ny = y + dy
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            di = di_mp(di, flag)
            dx, dy = direction[di]
            x += dx
            y += dy
        else:
            x = nx
            y = ny

R, C, T = map(int, input().split())
graph = []
up = 0
down = 0
for i in range(R):
    row = list(map(int, input().split()))
    if row[0] == -1:
        if up == 0:
            up = i
        else:
            down = i
    graph.append(row)

for _ in range(T):
    ngraph = [[0] * C for _ in range(R)]
    for a in range(R):
        for b in range(C):
            if graph[a][b] > 0:
                expand(a, b, graph, ngraph)
    circulation(up, ngraph, False)
    circulation(down, ngraph, True)
    ngraph[up][0] = -1
    ngraph[down][0] = -1
    graph = ngraph
print(sum(map(sum, graph)) + 2)