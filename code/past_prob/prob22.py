direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def rev_di(di):
    if di % 2 == 0:
        return di + 1
    else:
        return di - 1

def shark_move(s, sz, g, ss):
    global direction
    global R
    global C
    x, y, sp, di = s
    dx, dy = direction[di]
    for _ in range(sp):
        nx = x + dx
        ny = y + dy
        if R > nx >= 0 and C > ny >= 0:
            x = nx
            y = ny
        else:
            di = rev_di(di)
            dx, dy = direction[di]
            x += dx
            y += dy
    if g[x][y] < sz:
        ss[g[x][y]] = []
        g[x][y] = sz
        ss[sz] = [x, y, sp, di]
    else:
        ss[sz] = []

R, C, M = map(int, input().split())
graph = [[0] * C for _ in range(R)]
sharks = [[] for _ in range(10001)]
for _ in range(M):
    r, c, speed, direct, size = map(int, input().split())
    graph[r - 1][c - 1] = size
    sharks[size] = [r - 1, c - 1, speed, direct - 1]


total = 0
for pos in range(C):
    close_size = 0
    for i in range(R):
        if graph[i][pos] != 0:
            close_size = graph[i][pos]
            break
    total += close_size
    if close_size != 0:
        sharks[close_size] = []
    graph = [[0] * C for _ in range(R)]
    for size in range(1, 10001):
        shark = sharks[size]
        if shark:
            shark_move(shark, size, graph, sharks)
print(total)