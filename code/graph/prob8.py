t = int(input())
for _ in range(t):
    n = int(input())
    last_year = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(n):
        for j in range(i + 1, n):
            graph[last_year[i]].append(last_year[j])
            indegree[last_year[j]] += 1
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1
        else:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1
    q = []
    for idx in range(1, n + 1):
        if indegree[idx] == 0:
            q.append(idx)
    cnt = 0
    res = []
    while q:
        cur = q.pop(0)
        cnt += 1
        res.append(cur)
        for e in graph[cur]:
            indegree[e] -= 1
            if indegree[e] == 0:
                q.append(e)
    if cnt == n:
        for team in res:
            print(team, end=' ')
        print('')
    else:
        print('IMPOSSIBLE')