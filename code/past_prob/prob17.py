def calc_chicken_len(h, c):
    global res
    total = 0
    for house in h:
        llst = []
        for chicken in c:
            llst.append(abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        total += min(llst)
    res = min(res, total)

def leave_chickens(h, c, ac):
    global M
    if len(ac) == M:
        calc_chicken_len(h, ac)
    else:
        if len(c) + len(ac) >= M:
            chicken = c.pop()
            ac.append(chicken)
            leave_chickens(h ,c, ac)
            ac.pop()
            leave_chickens(h, c, ac)
            c.append(chicken)

N, M = map(int, input().split())
houses = []
chickens = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            houses.append((i, j))
        elif row[j] == 2:
            chickens.append((i, j))
res = int(1e9)
leave_chickens(houses, chickens, [])
print(res)