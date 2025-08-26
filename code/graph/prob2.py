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
edges = []
parents = [0] * (n + 1)
total = 0
last_cost = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
for i in range(1, n + 1):
    parents[i] = i

for edge in edges:
    pa = find(parents, edge[1])
    pb = find(parents, edge[2])
    if pa != pb:
        union(parents, edge[1], edge[2])
        total += edge[0]
        last_cost = edge[0]

print(total - last_cost)