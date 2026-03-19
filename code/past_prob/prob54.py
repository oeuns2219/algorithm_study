direct = [(-1, 1), (0, 1), (1, 1)]

def find_way(x, y, g):
    global R, C, cnt, direct
    if y == C - 1:
        cnt += 1
        g[x][y] = 'x'
        return True
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if R > nx >= 0 and C > ny >= 0 and g[nx][ny] == '.':
            if find_way(nx, ny, g):
                g[x][y] = 'x'
                return True
    g[x][y] = 'x'
    return False

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))

cnt = 0
for start in range(R):
    find_way(start, 0, graph)

print(cnt)