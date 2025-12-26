import copy

direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def move(fs, sm, sa, sb):
    global direction
    new_fs = [[[] for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            if fs[a][b]:
                for di in fs[a][b]:
                    ori_di = di
                    da, db = direction[di]
                    na, nb = a + da, b + db
                    if not (4 > na >= 0 and 4 > nb >= 0 and not sm[na][nb] and not (na == sa and nb == sb)):
                        di = (di - 1) % 8
                        da, db = direction[di]
                        na, nb = a + da, b + db
                        while not (4 > na >= 0 and 4 > nb >= 0 and not sm[na][nb] and not (na == sa and nb == sb)) and di != ori_di:
                            di = (di - 1) % 8
                            da, db = direction[di]
                            na, nb = a + da, b + db
                    if 4 > na >= 0 and 4 > nb >= 0 and not sm[na][nb] and not (na == sa and nb == sb):
                        new_fs[na][nb].append(di)
                    else:
                        new_fs[a][b].append(di)
    return new_fs

def poss_move(fs, sa, sb, fish_cnt, move_cnt, val):
    global max_cnt
    global min_val
    global direct

    if move_cnt == 3:
        if fish_cnt > max_cnt:
            max_cnt = fish_cnt
            min_val = val
        elif fish_cnt == max_cnt and val < min_val:
            min_val = val
    else:
        for j in range(4):
            da, db = direct[j]
            na, nb = sa + da, sb + db
            if 4 > na >= 0 and 4 > nb >= 0:
                buffer = fs[na][nb]
                fs[na][nb] = []
                poss_move(fs, na, nb, fish_cnt + len(buffer), move_cnt + 1, val + ((j + 1) * (10 ** (2 - move_cnt))))
                fs[na][nb] = buffer

def shark_move(sa, sb, mv, fs, sm, sm_lst, iter_num):
    global direct
    directs = [(mv // 100) - 1, ((mv % 100) // 10) - 1, (mv % 10) - 1]
    for di in directs:
        da, db = direct[di]
        sa += da
        sb += db
        if fs[sa][sb]:
            fs[sa][sb] = []
            if sm[sa][sb]:
                for j in range(len(sm_lst)):
                    a, b, _ = sm_lst[j]
                    if a == sa and b == sb:
                        sm_lst[j][2] = iter_num
            else:
                sm[sa][sb] = True
                sm_lst.append([sa, sb, iter_num])
    return sa, sb

M, S = map(int, input().split())
fishes = [[[] for _ in range(4)] for _ in range(4)]
smell = [[False] * 4 for _ in range(4)]
smell_lst = []
for _ in range(M):
    fx, fy, d = map(int, input().split())
    fishes[fx - 1][fy - 1].append(d - 1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1

for i in range(S):
    copy_fishes = copy.deepcopy(fishes)
    fishes = move(fishes, smell, sx, sy)
    max_cnt = -1
    min_val = int(1e9)
    poss_move(fishes, sx, sy, 0, 0, 0)
    sx, sy = shark_move(sx, sy, min_val, fishes, smell, smell_lst, i)
    new_smell_lst = []
    for x, y, time in smell_lst:
        if time == i - 2:
            smell[x][y] = False
        else:
            new_smell_lst.append([x, y, time])
    smell_lst = new_smell_lst
    fishes = [[e1 + e2 for e1, e2 in zip(e_lst1, e_lst2)] for e_lst1, e_lst2 in zip(fishes, copy_fishes)]
fish_cnt = [[len(lst2) for lst2 in lst1] for lst1 in fishes]
print(sum(map(sum, fish_cnt)))