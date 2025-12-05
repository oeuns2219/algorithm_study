direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def roll(b):
    global N
    num = 1
    cnt = 0
    while num < N * N:
        if b[num] == 0:
            cnt += 1
        else:
            if cnt > 0:
                b[num], b[num - cnt] = b[num - cnt], b[num]
        num += 1

def explode(b, ec):
    global N
    if b[1] == 0:
        return False
    num = 2
    prev = b[1]
    cnt = 1
    is_explode = False
    while num < N * N:
        if b[num] == prev:
            cnt += 1
        else:
            if cnt >= 4:
                is_explode = True
                ec[prev - 1] += cnt
                for j in range(1, cnt + 1):
                    b[num - j] = 0
            if b[num] == 0:
                break
            prev = b[num]
            cnt = 1
        num += 1
    return is_explode

def change(b):
    global N
    if b[1] == 0:
        return
    num = 2
    prev = b[1]
    cnt = 1
    lst = []
    while num < N * N:
        if b[num] == prev:
            cnt += 1
        else:
            lst.append(cnt)
            lst.append(prev)
            if b[num] == 0:
                break
            prev = b[num]
            cnt = 1
        num += 1

    for j in range(1, N * N):
        if j > len(lst):
            b[j] = 0
        else:
            b[j] = lst[j - 1]

N, M = map(int, input().split())
grid = []
bag = [-1] * (N * N)
for _ in range(N):
    grid.append(list(map(int, input().split())))

x, y = N // 2, N // 2
idx = 1
move = 1
end = False
while True:
    if move % 2 == 1:
        dx, dy = direction[2]
        for _ in range(move):
            x += dx
            y += dy
            bag[idx] = grid[x][y]
            grid[x][y] = idx
            idx += 1
            if x == 0 and y == 0:
                end = True
                break
        if end:
            break
        dx, dy = direction[1]
        for _ in range(move):
            x += dx
            y += dy
            bag[idx] = grid[x][y]
            grid[x][y] = idx
            idx += 1
        move += 1
    else:
        dx, dy = direction[3]
        for _ in range(move):
            x += dx
            y += dy
            bag[idx] = grid[x][y]
            grid[x][y] = idx
            idx += 1

        dx, dy = direction[0]
        for _ in range(move):
            x += dx
            y += dy
            bag[idx] = grid[x][y]
            grid[x][y] = idx
            idx += 1
        move += 1

ex_cnt = [0] * 3
x, y = N // 2, N // 2
for _ in range(M):
    di, si = map(int, input().split())
    dx, dy = direction[di - 1]
    for i in range(1, si + 1):
        nx, ny = x + (i * dx), y + (i * dy)
        bag[grid[nx][ny]] = 0
    roll(bag)
    while explode(bag, ex_cnt):
        roll(bag)
    change(bag)
score = (1 * ex_cnt[0]) + (2 * ex_cnt[1]) + (3 * ex_cnt[2])
print(score)