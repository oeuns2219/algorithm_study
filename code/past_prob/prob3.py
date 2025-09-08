direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def int_minus(e):
    return int(e) - 1

def is_empty(s_graph, x, y, t):
    global k
    if s_graph[x][y][0] == 0 or (t - s_graph[x][y][1]) > k:
        return True
    else:
        return False

def rev_direct(di):
    if di == 0 or di == 2:
        return di + 1
    else:
        return di - 1

def shark_move(s_alive, s_pos, s_priority, s_graph, t):
    global direct
    global n
    global m
    for shark in s_alive:
        find = False
        x, y, di = s_pos[shark]
        priority = s_priority[shark][di]
        for new_di in priority:
            dx, dy = direct[new_di]
            new_x = x + dx
            new_y = y + dy
            if n > new_x >= 0 and n > new_y >= 0 and is_empty(s_graph, new_x, new_y, t):
                s_pos[shark][0] = new_x
                s_pos[shark][1] = new_y
                s_pos[shark][2] = new_di
                find = True
                break
        if not find:
            for new_di in priority:
                dx, dy = direct[new_di]
                new_x = x + dx
                new_y = y + dy
                if n > new_x >= 0 and n > new_y >= 0 and s_graph[new_x][new_y][0] == shark:
                    s_pos[shark][0] = new_x
                    s_pos[shark][1] = new_y
                    s_pos[shark][2] = new_di
                    break
    pos_set = set()
    for i in range(1, m + 1):
        x, y, _ = s_pos[i]
        if (x, y) in pos_set and x != -1 and y != -1:
            s_pos[i][0] = -1
            s_pos[i][1] = -1
            s_alive.remove(i)
        else:
            pos_set.add((x, y))
    for shark in s_alive:
        x, y, _ = s_pos[shark]
        s_graph[x][y] = (shark, t)

n, m, k = map(int, input().split())
shark_alive = list(range(1, m + 1))
shark_pos = [[] for _ in range(m + 1)]
shark_priority = [[] for _ in range(m + 1)]
smell_graph = [[(0, 0)] * n for _ in range(n)]
time = 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] != 0:
            shark_pos[row[j]].append(i)
            shark_pos[row[j]].append(j)
            smell_graph[i][j] = (row[j], time)
shark_direct = list(map(int, input().split()))
for i in range(m):
    shark_pos[i + 1].append(shark_direct[i] - 1)
for i in range(1, m + 1):
    for _ in range(4):
        shark_priority[i].append(list(map(int_minus, input().split())))
while len(shark_alive) != 1 and time <= 1000:
    time += 1
    shark_move(shark_alive, shark_pos, shark_priority, smell_graph, time)
if time > 1000:
    print(-1)
else:
    print(time)