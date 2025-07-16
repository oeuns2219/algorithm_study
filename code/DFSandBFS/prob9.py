n, l, r = map(int, input().split())
world = []
for _ in range(n):
    world.append(list(map(int, input().split())))

res = 0
move = True
while move:
    move = False
    borders = [[[False] * 4 for _ in range(n)] for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i + 1 < n:
                diff = abs(world[i][j] - world[i + 1][j])
                if l <= diff <= r:
                    move = True
                    borders[i][j][2] = True
                    borders[i + 1][j][0] = True

            if j + 1 < n:
                diff = abs(world[i][j] - world[i][j + 1])
                if l <= diff <= r:
                    move = True
                    borders[i][j][1] = True
                    borders[i][j + 1][3] = True

    if move:
        res += 1
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    cnt = 0
                    total = 0
                    union = [(i, j)]
                    queue = [(i, j)]
                    visited[i][j] = True
                    while len(queue) != 0:
                        cnt += 1
                        x, y = queue.pop(0)
                        total += world[x][y]
                        if borders[x][y][0] and not visited[x - 1][y]:
                            union.append((x - 1, y))
                            queue.append((x - 1, y))
                            visited[x - 1][y] = True

                        if borders[x][y][1] and not visited[x][y + 1]:
                            union.append((x, y + 1))
                            queue.append((x, y + 1))
                            visited[x][y + 1] = True

                        if borders[x][y][2] and not visited[x + 1][y]:
                            union.append((x + 1, y))
                            queue.append((x + 1, y))
                            visited[x + 1][y] = True

                        if borders[x][y][3] and not visited[x][y - 1]:
                            union.append((x, y - 1))
                            queue.append((x, y - 1))
                            visited[x][y - 1] = True

                    if cnt != 1:
                        population = total // cnt
                        for cx, cy in union:
                            world[cx][cy] = population

print(res)