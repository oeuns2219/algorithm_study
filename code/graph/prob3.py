n = int(input())
graph = [[] for _ in range(n + 1)]
rev_graph = [[]]
indegree = [0] * (n + 1)
total_time = [0] * (n + 1)
for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    total_time[i] = lst[0]
    rev_graph.append(lst[1:-1])
    indegree[i] = len(lst[1:-1])
    for j in lst[1:-1]:
        graph[j].append(i)

q = []
for k in range(1, n + 1):
    if indegree[k] == 0:
        q.append(k)

while q:
    cur = q.pop(0)
    for e in graph[cur]:
        indegree[e] -= 1
        if indegree[e] == 0:
            q.append(e)

    if rev_graph[cur]:
        lst = [total_time[e] for e in rev_graph[cur]]
        total_time[cur] += max(lst)

for l in range(1, n + 1):
    print(total_time[l])