def cal_chicken(h, c):
    global n
    dists = []
    for house in h:
        dist = 2 * n
        for chicken in c:
            dist = min(dist, abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
        dists.append(dist)
    return sum(dists)

def minus_chicken(h, c, x):
    dists = []

    for chicken in c:
        nc = c.copy()
        nc.remove(chicken)
        if x == 1:
            dists.append(cal_chicken(h, nc))
        else:
            dists.append(minus_chicken(h, nc, x-1))
    return min(dists)

n, m = map(int, input().split())
houses = []
chickens = []
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] == 1:
            houses.append((i, j))
        elif lst[j] == 2:
            chickens.append((i, j))

delta = len(chickens) - m
if delta:
    print(minus_chicken(houses, chickens, delta))
else:
    print(cal_chicken(houses, chickens))