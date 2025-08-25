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

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    is_same, a, b = map(int, input().split())
    if is_same:
        if find(parent, a) == find(parent, b):
            print('YES')
        else:
            print('NO')
    else:
        union(parent, a, b)