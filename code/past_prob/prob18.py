translation = {'U': 0, 'D': 1, 'F': 2, 'B': 3, 'L': 4, 'R': 5}
T = int(input())
for _ in range(T):
    sides = [['w'] * 9, ['y'] * 9, ['r'] * 9, ['o'] * 9, ['g'] * 9, ['b'] * 9]
    connected = [[(3, [2, 1, 0]), (5, [2, 1, 0]), (2, [2, 1, 0]), (4, [2, 1, 0])],
                 [(3, [6, 7, 8]), (4, [6, 7, 8]), (2, [6, 7, 8]), (5, [6, 7, 8])],
                 [(0, [6, 7, 8]), (5, [0, 3, 6]), (1, [6, 7, 8]), (4, [8, 5, 2])],
                 [(0, [2, 1, 0]), (4, [0, 3, 6]), (1, [2, 1, 0]), (5, [8, 5, 2])],
                 [(0, [0, 3, 6]), (2, [0, 3, 6]), (1, [8, 5, 2]), (3, [8, 5, 2])],
                 [(0, [8, 5, 2]), (3, [0, 3, 6]), (1, [0, 3, 6]), (2, [8, 5, 2])]]
    N = int(input())
    orders = list(input().split())
    for order in orders:
        side = translation[order[0]]
        if order[1] == '+':
            sides[side][0], sides[side][6] = sides[side][6], sides[side][0]
            sides[side][6], sides[side][8] = sides[side][8], sides[side][6]
            sides[side][8], sides[side][2] = sides[side][2], sides[side][8]
            sides[side][1], sides[side][3] = sides[side][3], sides[side][1]
            sides[side][3], sides[side][7] = sides[side][7], sides[side][3]
            sides[side][7], sides[side][5] = sides[side][5], sides[side][7]
            buf = []
            side_num = connected[side][3][0]
            for idx in connected[side][3][1]:
                buf.append(sides[side_num][idx])
            for side_num, lst in connected[side]:
                for i in range(3):
                    buf[i], sides[side_num][lst[i]] = sides[side_num][lst[i]], buf[i]
        else:
            sides[side][0], sides[side][2] = sides[side][2], sides[side][0]
            sides[side][2], sides[side][8] = sides[side][8], sides[side][2]
            sides[side][8], sides[side][6] = sides[side][6], sides[side][8]
            sides[side][1], sides[side][5] = sides[side][5], sides[side][1]
            sides[side][5], sides[side][7] = sides[side][7], sides[side][5]
            sides[side][7], sides[side][3] = sides[side][3], sides[side][7]
            buf = []
            side_num = connected[side][0][0]
            for idx in connected[side][0][1]:
                buf.append(sides[side_num][idx])
            for ri in range(3, -1, -1):
                side_num, lst = connected[side][ri]
                for i in range(3):
                    buf[i], sides[side_num][lst[i]] = sides[side_num][lst[i]], buf[i]
    for a in range(3):
        for b in range(3):
            print(sides[0][(3 * a) + b], end='')
        print('')