from collections import deque

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_exist(g):
    global N, M
    sum_lst = [sum(l) for l in g]
    return sum(sum_lst) != -(N * M)

def melt(g):
    global N, M, direct
    for n in range(1, N - 1):
        for m in range(1, M - 1):
            cnt = 0
            if g[n][m] == 1:
                for dn, dm in direct:
                    nn, nm = n + dn, m + dm
                    if g[nn][nm] == -1:
                        cnt += 1
            if cnt >= 2:
                g[n][m] = 0

def outside(g):
    global N, M, direct
    q = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    g[0][0] = -1
    while q:
        cn, cm = q.popleft()
        for dn, dm in direct:
            nn, nm = cn + dn, cm + dm
            if N > nn >= 0 and M > nm >= 0 and (g[nn][nm] == -1 or g[nn][nm] == 0) and not visited[nn][nm]:
                q.append((nn, nm))
                visited[nn][nm] = True
                g[nn][nm] = -1

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

T = 0
outside(graph)
while is_exist(graph):
    T += 1
    melt(graph)
    outside(graph)
print(T)