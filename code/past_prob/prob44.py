from collections import deque

INF = int(1e9)

def bfs(graph, visited, usado, start, min_val):
    visited[start] = True
    que = deque([[start, min_val]])
    while que:
        current, u = que.popleft()
        if start != current and usado[start][current] == 0:
            usado[start][current] = u
        for j in graph[current]:
            if not visited[j]:
                visited[j] = True
                que.append([j, min(u, usado[current][j])])

N, Q = map(int, input().split())
U = [[0] * N for _ in range(N)]
G = [[] for _ in range(N)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    U[p - 1][q - 1] = r
    U[q - 1][p - 1] = r
    G[p - 1].append(q - 1)
    G[q -1].append(p - 1)
for _ in range(Q):
    K, V = map(int, input().split())
    cnt = 0
    v = [False] * N
    bfs(G, v, U, V - 1, INF)
    for q in range(N):
        if U[V - 1][q] >= K:
            cnt += 1
    print(cnt)