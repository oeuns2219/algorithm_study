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

n = int(input())
parents = [0] * n
for i in range(n):
    parents[i] = i
x_coordinates = []
y_coordinates = []
z_coordinates = []
edges = []
for idx in range(n):
    coordinate = list(map(int, input().split()))
    x_coordinates.append((coordinate[0], idx))
    y_coordinates.append((coordinate[1], idx))
    z_coordinates.append((coordinate[2], idx))
x_coordinates.sort()
y_coordinates.sort()
z_coordinates.sort()

for j in range(n - 1):
    edges.append((x_coordinates[j + 1][0] - x_coordinates[j][0], x_coordinates[j][1], x_coordinates[j + 1][1]))
    edges.append((y_coordinates[j + 1][0] - y_coordinates[j][0], y_coordinates[j][1], y_coordinates[j + 1][1]))
    edges.append((z_coordinates[j + 1][0] - z_coordinates[j][0], z_coordinates[j][1], z_coordinates[j + 1][1]))

edges.sort()
total = 0
for edge in edges:
    if find(parents, edge[1]) != find(parents, edge[2]):
        union(parents, edge[1], edge[2])
        total += edge[0]
print(total)