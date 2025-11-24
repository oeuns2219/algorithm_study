from collections import deque
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N = int(input())
students = deque([])
wish_list = [[] for _ in range((N ** 2) + 1)]
for _ in range(N ** 2):
    n, w1, w2, w3, w4 = map(int, input().split())
    students.append(n)
    wish_list[n].append(w1)
    wish_list[n].append(w2)
    wish_list[n].append(w3)
    wish_list[n].append(w4)
classroom = [[-1] * (N + 2)]
for _ in range(N):
    classroom.append([-1] + [0] * N + [-1])
classroom.append([-1] * (N + 2))
while students:
    student = students.popleft()
    wish_match = [[] for _ in range(5)]
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if classroom[x][y] != 0:
                continue
            cnt = 0
            for dx, dy in direction:
                if classroom[x + dx][y + dy] in wish_list[student]:
                    cnt += 1
            wish_match[cnt].append((x, y))
    more_space = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    cur = 4
    while len(wish_match[cur]) == 0:
        cur -= 1
    if len(wish_match[cur]) > 1:
        for x, y in wish_match[cur]:
            cnt = 0
            for dx, dy in direction:
                if classroom[x + dx][y + dy] == 0:
                    cnt += 1
            if more_space[cnt] == (0, 0):
                more_space[cnt] = (x, y)
        space = 4
        while more_space[space] == (0, 0):
            space -= 1
        nx, ny = more_space[space]
        classroom[nx][ny] = student
    else:
        nx, ny = wish_match[cur][0]
        classroom[nx][ny] = student

total = 0
score = [0, 1, 10, 100, 1000]
for x in range(1, N + 1):
    for y in range(1, N + 1):
        cnt = 0
        for dx, dy in direction:
            if classroom[x + dx][y + dy] in wish_list[classroom[x][y]]:
                cnt += 1
        total += score[cnt]
print(total)