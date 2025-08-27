n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
score = [0] * (n + 1)
route = [[] for _ in range(n + 1)]
for _ in range(m):
    p, q, r = map(int, input().split())
    graph[p].append(q)
    rev_graph[q].append((p, r))
    indegree[q] += 1

q = [1]
start = True
while q:
    cur = q.pop(0)
    if start:
        start = False
        route[cur] += [cur]
    else:
        lst = [(score[e[0]] + e[1], e[0]) for e in rev_graph[cur]]
        lst.sort(key=lambda e: -e[0])
        score[cur] = lst[0][0]
        route[cur] = route[lst[0][1]] + [cur]
        if cur == 1:
            break
    for num in graph[cur]:
        indegree[num] -= 1
        if indegree[num] == 0:
            q.append(num)

print(score[1])
for k in route[1]:
    print(k, end=' ')