def check(g):
    global n
    global h
    for x in range(n):
        cur = x
        for y in range(h):
            if g[y][cur] != 0:
                cur = g[y][cur] - 1
        if cur != x:
            return False
    return True

def add_ladder(g, num):
    global n
    global h
    global success
    if num:
        for x in range(n - 1):
            for y in range(h):
                if g[y][x] == 0 and g[y][x + 1] == 0:
                    g[y][x] = x + 2
                    g[y][x + 1] = x + 1
                    add_ladder(g, num - 1)
                    g[y][x] = 0
                    g[y][x + 1] = 0
    else:
        if check(g):
            success = True

n, m, h = map(int, input().split())
graph = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = b + 1
    graph[a - 1][b] = b

success = False
add_ladder(graph, 0)
if success:
    print(0)
else:
    add_ladder(graph, 1)
    if success:
        print(1)
    else:
        add_ladder(graph, 2)
        if success:
            print(2)
        else:
            add_ladder(graph, 3)
            if success:
                print(3)
            else:
                print(-1)