def left_d(org_d):
    if org_d == 0: return 3
    else: return org_d-1

def travel(x, y, fd, d, cnt):
    global game_map
    global pos_delta
    global back_delta
    global n
    global m
    game_map[x][y] = -1
    new_d = left_d(d)
    new_x = x + pos_delta[new_d][0]
    new_y = y + pos_delta[new_d][1]
    if game_map[new_x][new_y] == 1 or game_map[new_x][new_y] == -1:
        if new_d == fd:
            back_x = x + back_delta[new_d][0]
            back_y = y + back_delta[new_d][1]
            if game_map[back_x][back_y] != 1:
                return travel(back_x, back_y, fd, new_d, cnt)
            else: return cnt
        else: return travel(x, y, fd, new_d, cnt)
    else: return travel(new_x, new_y, new_d, new_d, cnt + 1)


n, m = map(int, input().split())
x_cor, y_cor ,direction = map(int, input().split())
pos_delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
back_delta = [(1, 0), (0, -1), (-1, 0), (0, 1)]
game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))

print(travel(x_cor, y_cor, direction, direction, 1))
