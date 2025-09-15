direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def int_minus(e):
    return int(e) - 1

def dice_move(c, d):
    global up
    global down
    global left
    global right
    oc = 7 - c
    if d == 0:
        right = c
        c = left
        left = oc
    elif d == 1:
        left = c
        c = right
        right = oc
    elif d == 2:
        up = c
        c = down
        down = oc
    else:
        down = c
        c = up
        up = oc
    return c

n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dice = [0] * 7
cur = 1
up = 2
down = 5
left = 4
right = 3
commands = list(map(int_minus, input().split()))
for command in commands:
    dx, dy = direction[command]
    nx = x + dx
    ny = y + dy
    if n > nx >= 0 and m > ny >= 0:
        x, y = nx, ny
        cur = dice_move(cur, command)
        print(dice[cur])
        other_side = 7 - cur
        if graph[x][y] == 0:
            graph[x][y] = dice[other_side]
        else:
            dice[other_side] = graph[x][y]
            graph[x][y] = 0