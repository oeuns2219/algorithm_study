direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_safe(g, s):
    global N, direct
    res = True
    for x, y in s:
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            while N > nx >= 0 and N > ny >= 0:
                if g[nx][ny] == 'O':
                    break
                if g[nx][ny] == 'T':
                    res = False
                    break
                nx += dx
                ny += dy
            if not res:
                return res
    return res

def make_obstacle(g, s, cnt, bx, by):
    global N
    if cnt == 3:
        return is_safe(g, s)
    for x in range(N):
        for y in range(N):
            if (x > bx or y > by) and g[x][y] == 'X':
                g[x][y] = 'O'
                if make_obstacle(g, s, cnt + 1, x, y):
                    return True
                g[x][y] = 'X'
    return False

N = int(input())
graph = []
students = []
for i in range(N):
    lst = list(input().split())
    for j in range(N):
        if lst[j] == 'S':
            students.append([i, j])
    graph.append(lst)

if make_obstacle(graph, students, 0, -1, -1):
    print('YES')
else:
    print('NO')