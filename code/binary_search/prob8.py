from bisect import bisect_left, bisect_right

m, n, l = map(int, input().split())
hunt_lst = list(map(int, input().split()))
hunt_lst.sort()
animals = dict()
cnt = 0
for _ in range(n):
    a, b = map(int, input().split())
    if b <= l:
        left = bisect_left(hunt_lst, a - (l - b))
        right = bisect_right(hunt_lst, a + (l - b))
        if right - left > 0:
            cnt += 1

print(cnt)