n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []
lst = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
while q:
    cur = q.pop(0)
    lst.append(cur)
    for e in graph[cur]:
        indegree[e] -= 1
        if indegree[e] == 0:
            q.append(e)
for student in lst:
    print(student, end=' ')