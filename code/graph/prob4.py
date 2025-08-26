def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    px = find(parent, x)
    py = find(parent, y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

plan = list(map(int, input().split()))
parents = [0] * n
for i in range(n):
    parents[i] = i

for a in range(n):
    for b in range(a + 1, n):
        if graph[a][b] == 1:
            union(parents, a, b)

flag = True
root = find(parents, plan[0])
for k in range(1, m):
    if root != find(parents, plan[k]):
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')