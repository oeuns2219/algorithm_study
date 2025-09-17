n, l = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
res = 2 * n
for i in range(n):
    before = graph[i][0]
    same_len = 0
    broken = False
    for j in range(n):
        if before == graph[i][j]:
            same_len += 1
        elif abs(before - graph[i][j]) == 1:
            if before < graph[i][j]:
                if same_len < l:
                    res -= 1
                    broken = True
                    break
                else:
                    before = graph[i][j]
                    same_len = 1
            if before > graph[i][j]:
                if same_len < 0:
                    res -= 1
                    broken = True
                    break
                else:
                    before = graph[i][j]
                    same_len = 1 - l
        else:
            res -= 1
            broken = True
            break
    if not broken and same_len < 0:
        res -= 1

    before = graph[0][i]
    same_len = 0
    broken = False
    for j in range(n):
        if before == graph[j][i]:
            same_len += 1
        elif abs(before - graph[j][i]) == 1:
            if before < graph[j][i]:
                if same_len < l:
                    res -= 1
                    broken = True
                    break
                else:
                    before = graph[j][i]
                    same_len = 1
            if before > graph[j][i]:
                if same_len < 0:
                    res -= 1
                    broken = True
                    break
                else:
                    before = graph[j][i]
                    same_len = 1 - l
        else:
            res -= 1
            broken = True
            break
    if not broken and same_len < 0:
        res -= 1

print(res)