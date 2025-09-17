def get_idx(num):
    if num > 7:
        return num - 8
    elif num < 0:
        return num + 8
    else:
        return num

def get3or9(num, b):
    global graph
    global lst_12
    if b:
        return graph[num][get_idx(lst_12[num] + 2)]
    else:
        return graph[num][get_idx(lst_12[num] - 2)]

def turn(num, di, vi):
    vi[num] = True
    left = num - 1
    right = num + 1
    if left > 0 and not vi[left] and get3or9(num, False) != get3or9(left, True):
        turn(left, not di, vi)
    if right < 5 and not vi[right] and get3or9(num, True) != get3or9(right, False):
        turn(right, not di, vi)
    if di:
        lst_12[num] = get_idx(lst_12[num] - 1)
    else:
        lst_12[num] = get_idx(lst_12[num] + 1)

graph = [[0] * 8]
for _ in range(4):
    graph.append(list(map(int, input())))
lst_12 = [0] * 5
k = int(input())
for _ in range(k):
    visited = [False] * 5
    a, b = map(int, input().split())
    direct = b == 1
    turn(a, direct, visited)
score = 0
for i in range(4):
    if graph[i + 1][lst_12[i + 1]] == 1:
        score += 2 ** i
print(score)