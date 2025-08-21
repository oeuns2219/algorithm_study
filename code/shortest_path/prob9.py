INF = int(1e9)

def new_int(string):
    global INF
    integer = int(string)
    if integer == 0:
        return INF
    else:
        return integer

def int_to_01(integer):
    if integer == INF:
        return 0
    else:
        return 1

def new_map(lst):
    return list(map(int_to_01, lst))

n = int(input())
shortest_path = []
for _ in range(n):
    shortest_path.append(list(map(new_int, input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            shortest_path[a][b] = min(shortest_path[a][b], shortest_path[a][k] + shortest_path[k][b])

shortest_path = list(map(new_map, shortest_path))
for i in range(n):
    for j in range(n):
        print(shortest_path[i][j], end=' ')
    print('')