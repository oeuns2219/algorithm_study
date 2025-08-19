import heapq
INF = int(1e9)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
t = int(input())
for _ in range(t):
    n = int(input())
    shortest_path = [[INF] * n for _ in range(n)]
    q = []
    edges = []
    for _ in range(n):
        edges.append(list(map(int, input().split())))

    shortest_path[0][0] = edges[0][0]
    heapq.heappush(q, (edges[0][0], 0, 0))
    while q:
        cost, x, y = heapq.heappop(q)
        if cost > shortest_path[x][y]:
            continue
        for i in range(4):
            new_x = x + directions[i][0]
            new_y = y + directions[i][1]
            if n > new_x >= 0 and n > new_y >= 0:
                new_cost = edges[new_x][new_y] + cost
                if shortest_path[new_x][new_y] > new_cost:
                    shortest_path[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))

    print(shortest_path[n - 1][n - 1])