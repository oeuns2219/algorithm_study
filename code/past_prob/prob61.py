direct = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

R, C = map(int, input().split())
I = []
crazy = []
for x in range(R):
    row = input()
    for y in range(C):
        if row[y] == 'I':
            I = [x, y]
        elif row[y] == 'R':
            crazy.append([x, y])

route = list(map(int, input()))

cnt = 0
lose = False
for i in range(len(route)):
    dx, dy = direct[route[i] - 1]
    ix, iy = I[0] + dx, I[1] + dy
    I = [ix, iy]
    if [ix, iy] in crazy:
        cnt = i + 1
        lose = True
        break
    bomb = [[-1] * C for _ in range(R)]
    while crazy:
        cx, cy = crazy.pop()
        if ix > cx:
            cx += 1
        elif ix < cx:
            cx -= 1
        if iy > cy:
            cy += 1
        elif iy < cy:
            cy -= 1
        if cx == ix and cy == iy:
            cnt = i + 1
            lose = True
            break
        bomb[cx][cy] += 1
    if lose:
        break
    for x in range(R):
        for y in range(C):
            if bomb[x][y] == 0:
                crazy.append([x, y])

if lose:
    print('kraj', cnt)
else:
    for x in range(R):
        for y in range(C):
            if [x, y] == I:
                print('I', end='')
            elif [x, y] in crazy:
                print('R', end='')
            else:
                print('.', end='')
        print('')