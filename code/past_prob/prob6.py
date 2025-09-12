direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def di_change(di, char):
    if char == 'L':
        if di == 0:
            return 3
        else:
            return di - 1
    else:
        if di == 3:
            return 0
        else:
            return di + 1

n = int(input())
k = int(input())
graph = [[1] * (n + 2)]
for _ in range(n):
    graph.append([1] + [0] * n + [1])
graph.append([1] * (n + 2))
graph[1][1] = 2
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 3
l = int(input())
di_change_lst = []
for _ in range(l):
    x, c = input().split()
    di_change_lst.append((int(x), c))
cur_head_x = 1
cur_head_y = 1
cur_head_di = 0
cur_tail_x = 1
cur_tail_y = 1
di_stack = []
cur_change = di_change_lst.pop(0)
time = 0
while True:
    time += 1
    dx, dy = direct[cur_head_di]
    di_stack.append(cur_head_di)
    cur_head_x += dx
    cur_head_y += dy
    if graph[cur_head_x][cur_head_y] == 0:
        graph[cur_head_x][cur_head_y] = 2
        tdx, tdy = direct[di_stack.pop(0)]
        graph[cur_tail_x][cur_tail_y] = 0
        cur_tail_x += tdx
        cur_tail_y += tdy
    elif graph[cur_head_x][cur_head_y] == 3:
        graph[cur_head_x][cur_head_y] = 2
    else:
        break
    if time == cur_change[0]:
        cur_head_di = di_change(cur_head_di, cur_change[1])
        if di_change_lst:
            cur_change = di_change_lst.pop(0)
        else:
            cur_change = (-1, 'D')
print(time)