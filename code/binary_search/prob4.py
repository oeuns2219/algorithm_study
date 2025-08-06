n = int(input())
seq = list(map(int, input().split()))

start = 0
end = n - 1
res = -1
while start <= end:
    mid = (start + end) // 2
    if mid == seq[mid]:
        res = mid
        break
    elif mid > seq[mid]:
        start = mid + 1
    else:
        end = mid - 1
print(res)