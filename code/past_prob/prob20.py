from collections import deque

near = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

N, M, K = map(int, input().split())
A = []
ground = [[5] * N for _ in range(N)]
trees = []
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    a, b, c = map(int, input().split())
    trees.append([c, a - 1, b - 1])
trees.sort()
trees = deque(trees)
for _ in range(K):
    dead_trees = []
    new_trees = deque()
    for _ in range(len(trees)):
        age, x, y = trees.popleft()
        if ground[x][y] >= age:
            ground[x][y] -= age
            new_trees.append([age + 1, x, y])
        else:
            dead_trees.append([age, x ,y])
    trees = new_trees

    for age, x, y in dead_trees:
        ground[x][y] += age // 2

    new_trees = deque()
    for age, x, y in trees:
        if age % 5 == 0:
            for dx, dy in near:
                nx = x + dx
                ny = y + dy
                if N > nx >= 0 and N > ny >= 0:
                    new_trees.append([1, nx, ny])
    new_trees.extend(trees)
    trees = new_trees

    for x in range(N):
        for y in range(N):
            ground[x][y] += A[x][y]
print(len(trees))