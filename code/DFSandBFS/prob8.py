def safe(h, s):
    global n
    res = True
    for x, y in s:
        north = True
        east = True
        south = True
        west = True
        cnt = 1
        while north or east or south or west:
            if north:
                if x - cnt < 0:
                    north = False
                else:
                    if h[x - cnt][y] == 'O':
                        north = False
                    elif h[x - cnt][y] == 'T':
                        res = False
                        break

            if east:
                if y + cnt >= n:
                    east = False
                else:
                    if h[x][y + cnt] == 'O':
                        east = False
                    elif h[x][y + cnt] == 'T':
                        res = False
                        break

            if south:
                if x + cnt >= n:
                    south = False
                else:
                    if h[x + cnt][y] == 'O':
                        south = False
                    elif h[x + cnt][y] == 'T':
                        res = False
                        break

            if west:
                if y - cnt < 0:
                    west = False
                else:
                    if h[x][y - cnt] == 'O':
                        west = False
                    elif h[x][y - cnt] == 'T':
                        res = False
                        break

            cnt += 1
        if not res:
            break
    return res

def install(h, s, k):
    global n

    if k == 3:
        return safe(h, s)
    else:
        for x in range(n):
            for y in range(n):
                if h[x][y] == 'X':
                    h[x][y] = 'O'
                    if install(h, s, k + 1):
                        return True
                    h[x][y] = 'X'
    return False

n = int(input())
hallway = []
students = []
for i in range(n):
    hallway.append(list(input().split()))
    for j in range(n):
        if hallway[i][j] == 'S':
            students.append((i, j))

if install(hallway, students, 0):
    print('YES')
else:
    print('NO')