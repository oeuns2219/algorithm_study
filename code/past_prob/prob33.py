direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[r - 1][c - 1].append([m, s, d])

for _ in range(K):
    ngraph = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            while graph[i][j]:
                m, s, d = graph[i][j].pop()
                di, dj = direction[d]
                ni = i + (di * (s % N))
                nj = j + (dj * (s % N))
                if ni < 0:
                    ni += N
                elif ni >= N:
                    ni -= N
                if nj < 0:
                    nj += N
                elif nj >= N:
                    nj -= N
                ngraph[ni][nj].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(ngraph[i][j]) > 1:
                all_even = True
                all_odd = True
                tm = 0
                ts = 0
                cnt = len(ngraph[i][j])
                while ngraph[i][j]:
                    m, s, d = ngraph[i][j].pop()
                    tm += m
                    ts += s
                    all_even = all_even and d % 2 == 0
                    all_odd = all_odd and d % 2 == 1
                nm = tm // 5
                ns = ts // cnt
                if nm == 0:
                    continue
                if all_even or all_odd:
                    for k in range(4):
                        ngraph[i][j].append([nm, ns, k * 2])
                else:
                    for k in range(4):
                        ngraph[i][j].append([nm, ns, (k * 2) + 1])
    graph = ngraph
total = 0
for i in range(N):
    for j in range(N):
        while graph[i][j]:
            m, _, _ = graph[i][j].pop()
            total += m
print(total)