def nearest(n, o, w):
    near = None
    dist = None
    change = 0
    half_n = n // 2
    for i in w:
        l0 = abs(i - o[0])
        l1 = abs(i - o[1])
        if l0 > half_n:
            l0 = n - l0
        if l1 > half_n:
            l1 = n - l1
        l = min((l0, l1))
        if l1 == l: change = 1
        if dist is None or dist > l:
            near = i
            dist = l
    return near, dist, change

def cover(l, d):
    res = -1
    for i in d:
        if i >= l:
            res = i
        else:
            break
    return res

def solution(n, weak, dist):
    m = len(dist)
    weak.sort()
    dist.sort(reverse = True)

    while len(weak) != 0:
        print(weak, dist)
        if len(dist) == 0: return -1
        friend = dist[-1]
        total = 0
        origin = [weak[0], weak[0]]
        weak.remove(origin[0])
        new_weak = weak.copy()
        while len(new_weak) != 0:
            near, length, change = nearest(n, origin, new_weak)
            new_friend = cover(total + length, dist)
            if new_friend == -1: break
            friend = new_friend
            new_weak.remove(near)
            total += length
            origin[change] = near
        dist.remove(friend)
        weak = new_weak
    print(weak, dist)
    return m - len(dist)

