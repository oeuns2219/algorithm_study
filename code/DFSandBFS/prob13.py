n = int(input())
graph = [[] for _ in range(n)]
parents = [-1] * n
parents[0] = 0
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

queue = [0]
while len(queue) != 0:
    k = queue.pop(0)
    for node in graph[k]:
        if parents[node] == -1:
            parents[node] = k
            queue.append(node)

parents = parents[1:]
for parent in parents:
    print(parent + 1)