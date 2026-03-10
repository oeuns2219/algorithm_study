direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def explode(b, n):
    global R
    global C
    global direction
    for x in range(R):
        for y in range(C):
            if b[x][y] == 'O':
                n[x][y] = '.'
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if R > nx >= 0 and C > ny >= 0:
                        n[nx][ny] = '.'

R, C, N = map(int, input().split())
before = []
for _ in range(R):
    before.append(list(input()))

now = before
T = 1
while T != N:
    T += 1
    if T % 2 == 0:
        before = now
        now = [['O'] * C for _ in range(R)]
    else:
        explode(before, now)

for i in range(R):
    for j in range(C):
        print(now[i][j], end='')
    print('')