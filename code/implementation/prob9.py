def change_d(d, s):
    new_d = d
    if s == 'L': new_d -= 1
    else: new_d += 1
    if new_d == -1: new_d = 3
    if new_d == 4: new_d = 0
    return new_d

n = int(input())
dummy_map = [[0]*n for _ in range(n)]
direction_map = [[0]*n for _ in range(n)] # 이것 보다 queue 를 사용한 것이 나음
direction_dct = dict()
d_lst = [(-1, 0), (0, 1), (1, 0), (0, -1)]
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    dummy_map[a-1][b-1] = 2
l = int(input())
for _ in range(l):
    t, d = input().split()
    t = int(t)
    direction_dct[t] = d

cur_t = 0
head_x = 0
head_y = 0
tail_x = 0
tail_y = 0
cur_d = 1 # 0:north, 1:east, 2:south, 3: west
dummy_map[0][0] = 1

while True:
    cur_t += 1
    direction_map[head_x][head_y] = cur_d
    head_x += d_lst[cur_d][0]
    head_y += d_lst[cur_d][1]
    if head_x < 0 or head_y < 0 or head_x >= n or head_y >= n or dummy_map[head_x][head_y] == 1:
        break
    else:
        if dummy_map[head_x][head_y] != 2:
            dummy_map[tail_x][tail_y] = 0
            tail_d = direction_map[tail_x][tail_y]
            tail_x += d_lst[tail_d][0]
            tail_y += d_lst[tail_d][1]
        dummy_map[head_x][head_y] = 1
        if cur_t in direction_dct:
            cur_d = change_d(cur_d, direction_dct[cur_t])

print(cur_t)