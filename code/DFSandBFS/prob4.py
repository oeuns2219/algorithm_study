def bfs(graph, start, height, width):
    queue = [start]
    while len(queue) != 0:
        x, y = queue.pop(0)
        if x > 0 and graph[x - 1][y] == 0:
            graph[x - 1][y] = 3
            queue.append((x-1, y))
        if y > 0 and graph[x][y - 1] == 0:
            graph[x][y - 1] = 3
            queue.append((x, y-1))
        if x < height - 1 and graph[x + 1][y] == 0:
            graph[x + 1][y] = 3
            queue.append((x+1, y))
        if y < width - 1 and graph[x][y + 1] == 0:
            graph[x][y + 1] = 3
            queue.append((x, y+1))

def count_safe(lab_map, height, width):
    for i in range(height):
        for j in range(width):
            if lab_map[i][j] == 2:
                lab_map[i][j] = 3
                bfs(lab_map, (i, j), height, width)

    cnt = 0
    for x in lab_map:
        for y in x:
            if y == 0: cnt += 1
    return cnt

n, m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

res = 0
for a in range(n):
    for b in range(m):
        if lab[a][b] == 0:
            for c in range(a, n):
                for d in range(m):
                    if lab[c][d] == 0 and ((a == c and d > b) or a != c):
                        for e in range(c, n):
                            for f in range(m):
                                if lab[e][f] == 0 and ((c == e and f > d) or c != e):
                                    lab_cpy = [elem[:] for elem in lab]
                                    lab_cpy[a][b] = 1
                                    lab_cpy[c][d] = 1
                                    lab_cpy[e][f] = 1
                                    res = max((res, count_safe(lab_cpy, n, m)))
print(res)