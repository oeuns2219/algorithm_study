t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    mine = list(map(int, input().split()))
    gold = [[0] * n for _ in range(m)]
    for i in range(n):
        gold[0][i] = mine[i * m]
    for x in range(1, m):
        for y in range(n):
            start = y - 1
            if start < 0:
                start = 0
            end = y + 2
            if end > n:
                end = n
            gold[x][y] = max(gold[x - 1][start:end]) + mine[x + (m * y)]
    print(max(gold[m-1]))