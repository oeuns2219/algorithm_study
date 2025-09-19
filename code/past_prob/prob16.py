direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def rev_and_rotate(di):
    di = (di + 2) % 4
    if di == 0:
        return 3
    else:
        return di - 1

def repeat_curve(g, dc, e):
    new_dc = []
    nx, ny = e
    for i in range(len(dc)):
        idx = -(i + 1)
        nd = rev_and_rotate(dc[idx])
        new_dc.append(nd)
        dx, dy = direction[nd]
        nx += dx
        ny += dy
        g[ny][nx] = 1
    return (nx, ny), new_dc

n = int(input())
graph = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    graph[y][x] = 1
    dragon_curve = [d]
    end = (x + direction[d][0], y + direction[d][1])
    graph[end[1]][end[0]] = 1
    for _ in range(g):
        end, new_dragon_curve = repeat_curve(graph, dragon_curve, end)
        dragon_curve += new_dragon_curve
cnt = 0
for a in range(100):
    for b in range(100):
        if graph[a][b] == 1 and graph[a + 1][b] == 1 and graph[a][b + 1] == 1 and graph[a + 1][b + 1] == 1:
            cnt += 1
print(cnt)