direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def rev_di(direct):
    return (direct + 2) % 4

def next_di(direct):
    return (direct + 1) % 4

def side_di(direct):
    n_direct = next_di(direct)
    return n_direct, rev_di(n_direct)

def add_sand(g, c_x, c_y, sand):
    global N
    global total
    if N > c_x >= 0 and N > c_y >= 0:
        g[c_x][c_y] += int(sand)
    else:
        total += int(sand)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
total = 0
x = (N - 1) // 2
y = (N - 1) // 2
di = 0
visited = [[False] * N for _ in range(N)]
visited[x][y] = True
while not(x == 0 and y == 0):
    dx, dy = direction[di]
    nx, ny = dx + x, dy + y
    rdi = rev_di(di)
    rdx, rdy = direction[rdi]
    sdi1, sdi2 = side_di(di)
    sdx1, sdy1 = direction[sdi1]
    sdx2, sdy2 = direction[sdi2]
    ori = graph[nx][ny]
    left = ori
    cx, cy = nx + (2 * dx), ny + (2 * dy)
    sw = int(ori * 0.05)
    add_sand(graph, cx, cy, sw)
    left -= sw
    cx, cy = nx + dx + sdx1, ny + dy + sdy1
    sw = int(ori * 0.1)
    add_sand(graph, cx, cy, sw)
    left -= sw
    cx, cy = nx + dx + sdx2, ny + dy + sdy2
    sw = int(ori * 0.1)
    add_sand(graph, cx, cy, sw)
    left -= sw
    cx, cy = nx + (2 * sdx1), ny + (2 * sdy1)
    sw = int(ori * 0.02)
    add_sand(graph, cx, cy, sw)
    left -= sw
    cx, cy = nx + sdx1, ny + sdy1
    sw = int(ori * 0.07)
    add_sand(graph, cx, cy, sw)
    left -= sw
    cx, cy = nx + (2 * sdx2), ny + (2 * sdy2)
    sw = int(ori * 0.02)
    add_sand(graph, cx, cy, sw)
    left -= sw
    cx, cy = nx + sdx2, ny + sdy2
    sw = int(ori * 0.07)
    add_sand(graph, cx, cy, sw)
    left -= sw
    cx, cy = nx + rdx + sdx1, ny + rdy + sdy1
    sw = int(ori * 0.01)
    add_sand(graph, cx, cy, sw)
    left -= sw
    cx, cy = nx + rdx + sdx2, ny + rdy + sdy2
    sw = int(ori * 0.01)
    add_sand(graph, cx, cy, sw)
    left -= sw
    cx, cy = nx + dx, ny + dy
    add_sand(graph, cx, cy, left)

    visited[nx][ny] = True
    ndi = next_di(di)
    ndx, ndy = direction[ndi]
    if not visited[nx + ndx][ny + ndy]:
        di = ndi
    x, y = nx, ny
print(total)