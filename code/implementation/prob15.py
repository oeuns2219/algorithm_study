def count_safe(lab_map, height, width):
    while True:
        change = False
        for i in range(height):
            for j in range(width):
                if lab_map[i][j] == 2:
                    if i > 0 and lab_map[i-1][j] == 0:
                        lab_map[i-1][j] = 2
                        change = True
                    if j > 0 and lab_map[i][j-1] == 0:
                        lab_map[i][j-1] = 2
                        change = True
                    if i < height - 1 and lab_map[i+1][j] == 0:
                        lab_map[i+1][j] = 2
                        change = True
                    if j < width - 1 and lab_map[i][j+1] == 0:
                        lab_map[i][j+1] = 2
                        change = True
        if not change: break

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