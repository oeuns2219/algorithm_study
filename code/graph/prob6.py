def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, x, y):
    px = find(p, x)
    py = find(p, y)
    if px < py:
        p[py] = px
    else:
        p[px] = py

n, m = map(int, input().split())
total = 0
parents = [0] * n
for i in range(n):
    parents[i] = i
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    total += c
    edges.append((c, a, b))
edges.sort()
min_total = 0
for edge in edges:
    if find(parents, edge[1]) != find(parents, edge[2]):
        union(parents, edge[1], edge[2])
        min_total += edge[0]
print(total - min_total)