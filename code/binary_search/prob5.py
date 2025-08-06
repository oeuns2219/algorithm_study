def count_house(houses, diff):
    global n
    k = houses[0] + diff
    num = 1
    i = 1
    while i < n:
        if houses[i] >= k:
            num += 1
            k = houses[i] + diff
        i += 1
    return num

n, c = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
start = 0
end = (lst[-1] - lst[0]) // (c - 1)
res = 0
while start <= end:
    mid = (start + end) // 2
    cnt = count_house(lst, mid)
    if cnt >= c:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)
