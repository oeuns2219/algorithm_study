connected = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def count_icecream(visit_table, pos):
    global n
    global m
    global connected
    visit_table[pos[0]][pos[1]] = True
    for direct in connected:
        x = direct[0] + pos[0]
        y = direct[1] + pos[1]
        if x >= 0 and y >= 0 and x < n and y < m and not visit_table[x][y]:
            count_icecream(visit_table, (x, y))

n, m = map(int, input().split())
mold = []
visited = [[False]*m for _ in range(n)]
cnt = 0

for i in range(n):
    row = list(map(int, input()))
    mold.append(row)
    for j in range(m):
        if row[j]:
            visited[i][j] = True

for a in range(n):
    for b in range(m):
        if not visited[a][b]:
            count_icecream(visited, (a, b))
            cnt += 1
print(cnt)