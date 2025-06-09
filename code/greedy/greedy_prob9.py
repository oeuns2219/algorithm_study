cycle = 0

def incline(elem):
    if elem != 0:
        return elem - cycle
    else: return elem

def solution(food_times, k):
    global cycle
    n = len(food_times)
    while True:
        tset = set(food_times)
        if 0 in tset: tset.remove(0)
        m = n - food_times.count(0)
        if len(tset) == 0:
            print(-1)
            return
        cycle = min(tset)
        if k >= m * cycle:
            k -= m * cycle
            food_times = list(map(incline, food_times))
        else:
            k %= m
            break

    res = 0
    while k != -1:
        if food_times[res] != 0:
            k -= 1
        res += 1

    print(res)

solution([3,2,1,0,3], 8)