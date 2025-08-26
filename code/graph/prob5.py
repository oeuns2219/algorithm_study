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

g = int(input())
p = int(input())
parents = [0] * (g + 1)
for i in range(g + 1):
    parents[i] = i

cnt = 0
for _ in range(p):
    gi = int(input())
    pgi = find(parents, gi)
    if pgi == 0:
        break
    cnt += 1
    union(parents, pgi, pgi - 1)

print(cnt)