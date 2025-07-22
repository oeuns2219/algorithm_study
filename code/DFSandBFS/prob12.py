def bfs(graph, start):
    queue = [start]
    nums = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while len(queue) != 0:
        x, y = queue.pop(0)
        for k in range(4):
            new_x = x + dx[k]
            new_y = y + dy[k]
            if graph[new_x][new_y] == 1:
                graph[new_x][new_y] = 0
                queue.append((new_x, new_y))
                nums += 1
    return nums

n = int(input())
town = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(n):
    row = list(map(int, input()))
    for j in range(n):
        town[i + 1][j + 1] = row[j]

cnt = 0
lst = []
for i in range(n):
    for j in range(n):
        a = i + 1
        b = j + 1
        if town[a][b] == 1:
            town[a][b] = 0
            cnt += 1
            lst.append(bfs(town, (a, b)))
lst.sort()
print(cnt)
for num in lst:
    print(num)