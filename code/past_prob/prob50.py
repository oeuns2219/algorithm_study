direct = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def move(ex, ca, cb, na, nb, d):
    size = len(ex) - 2
    if size < 4:
        size = 4
    collide = False
    min_t = int(2e8) + 1
    for idx in range(size):
        coa, cob, noa, nob = ex[idx]
        if d % 2 == 0:
            min_a, max_a = min(ca, na), max(ca, na)
            if cob == nob:
                if cb == cob:
                    min_oa, max_oa = min(coa, noa), max(coa, noa)
                    if min_oa <= min_a <= max_oa or min_a <= min_oa <= max_a:
                        collide = True
                        min_t = min(min_t, min(abs(ca - coa), abs(ca - noa)))
            else:
                min_ob, max_ob = min(cob, nob), max(cob, nob)
                if min_a <= coa <= max_a and min_ob <= cb <= max_ob:
                    collide = True
                    min_t = min(min_t, abs(ca - coa))
        else:
            min_b, max_b = min(cb, nb), max(cb, nb)
            if coa == noa:
                if ca == coa:
                    min_ob, max_ob = min(cob, nob), max(cob, nob)
                    if min_ob <= min_b <= max_ob or min_b <= min_ob <= max_b:
                        collide = True
                        min_t = min(min_t, min(abs(cb - cob), abs(cb - nob)))
            else:
                min_oa, max_oa = min(coa, noa), max(coa, noa)
                if min_b <= cob <= max_b and min_oa <= ca <= max_oa:
                    collide = True
                    min_t = min(min_t, abs(cb - cob))
    if collide:
        return min_t
    ex.append([ca, cb, na, nb])
    return 0


L = int(input())
N = int(input())
T = 0
exist = [[L + 1, L + 1, L + 1, -L], [L + 1, -(L + 1), -L, -(L + 1)], [-(L + 1), -(L + 1), -(L + 1), L], [-(L + 1), L + 1, L, L + 1]]
di = 0
cx, cy = 0, 0
dead = False
for _ in range(N):
    st, ddi = input().split()
    dt = int(st)
    dx, dy = direct[di]
    nx, ny = cx + (dt * dx), cy + (dt * dy)
    t = move(exist, cx, cy, nx, ny, di)
    if t != 0:
        T += t
        dead = True
        break
    T += dt
    if ddi == 'L':
        di = (di - 1) % 4
    else:
        di = (di + 1) % 4
    cx, cy = nx, ny
if dead:
    print(T)
else:
    if di % 2 == 0:
        nx, ny = exist[di][0], cy
    else:
        nx, ny = cx, exist[di][1]
    t = move(exist, cx, cy, nx, ny, di)
    T += t
    print(T)