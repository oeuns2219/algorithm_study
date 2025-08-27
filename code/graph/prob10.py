t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    delays = list(map(int, input().split()))
    total_delays = [0] * n
    graph = [[] for _ in range(n + 1)]
    rev_graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        rev_graph[y].append(x)
        indegree[y] += 1
    w = int(input())

    q = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        cur = q.pop(0)
        if len(rev_graph[cur]) == 0:
            total_delays[cur - 1] = delays[cur - 1]
        else:
            total_lst = [total_delays[e - 1] for e in rev_graph[cur]]
            total_delays[cur - 1] = max(total_lst) + delays[cur - 1]
        if cur == w:
            break
        for building in graph[cur]:
            indegree[building] -= 1
            if indegree[building] == 0:
                q.append(building)
    print(total_delays[w - 1])