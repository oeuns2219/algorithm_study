from bisect import bisect_left

direct = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
di_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

N, K = map(int, input().split())
di_lst = list(input())
plus = dict()
minus = dict()
x = -1
y = -1
for _ in range(N):
    a, b = map(int, input().split())
    if x == -1:
        x, y = a, b
    c = a - b
    d = a + b
    if c in plus:
        plus[c].append([a, b])
    else:
        plus[c] = [[a, b]]
    if d in minus:
        minus[d].append([a, b])
    else:
        minus[d] = [[a, b]]
for key in plus:
    plus[key].sort()
for key in minus:
    minus[key].sort()
for d in di_lst:
    di = di_dict[d]
    dx, dy = direct[di]
    if dx * dy > 0:
        is_plus = True
    else:
        is_plus = False
    pk = x - y
    mk = x + y
    pidx = bisect_left(plus[pk], [x, y])
    midx = bisect_left(minus[mk], [x, y])
    if is_plus:
        if dx > 0:
            if pidx < len(plus[pk]) - 1:
                x, y = plus[pk][pidx + 1]
                plus[pk].pop(pidx)
                minus[mk].pop(midx)
        else:
            if pidx > 0:
                x, y = plus[pk][pidx - 1]
                plus[pk].pop(pidx)
                minus[mk].pop(midx)
    else:
        if dx > 0:
            if midx < len(minus[mk]) - 1:
                x, y = minus[mk][midx + 1]
                plus[pk].pop(pidx)
                minus[mk].pop(midx)
        else:
            if midx > 0:
                x, y = minus[mk][midx - 1]
                plus[pk].pop(pidx)
                minus[mk].pop(midx)

print(x, y)
