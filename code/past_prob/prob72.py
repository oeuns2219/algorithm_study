

direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
di_dict = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
'''
백준 문제 풀이
2174 로봇 시뮬레이션
'''
A, B = map(int, input().split())
N, M = map(int, input().split())
graph = [[0] * A for _ in range(B)]
robot_lst = []
for i in range(N):
    a, b, d = input().split()
    x = B - int(b)
    y = int(a) - 1
    di = di_dict[d]
    graph[x][y] = i + 1
    robot_lst.append([x, y, di])
fail = False
for _ in range(M):
    a, order, b = input().split()
    robot = int(a) - 1
    x, y, di = robot_lst[robot]
    times = int(b)
    if order == 'L':
        di = (di - times) % 4
    elif order == 'R':
        di = (di + times) % 4

    if order != 'F':
        robot_lst[robot][2] = di
    else:
        cx, cy = x, y
        dx, dy = direct[di]
        for _ in range(times):
            nx, ny = cx + dx, cy + dy
            if not (B > nx >= 0 and A > ny >= 0):
                print('Robot %d crashes into the wall' % (robot + 1))
                fail = True
                break
            else:
                if graph[nx][ny] != 0:
                    print('Robot %d crashes into robot %d' % (robot + 1, graph[nx][ny]))
                    fail = True
                    break
                else:
                    graph[cx][cy] = 0
                    graph[nx][ny] = robot + 1
                    cx, cy = nx, ny
        robot_lst[robot][0] = cx
        robot_lst[robot][1] = cy
        if fail:
            break
if not fail:
    print('OK')