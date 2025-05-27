n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

arr.sort(reverse = True)
max1 = arr[0]
max2 = arr[1]

while m > 0:
    if m > k:
        res += k * max1 + max2
        m -= k + 1
    elif m == k:
        res += k * max1
        m -= k
    else:
        res += m * max1
        m -= m

print(res)