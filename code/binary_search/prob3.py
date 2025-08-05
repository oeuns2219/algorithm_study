def binary_search(lst, target, start, end, pos, flag):
    if start > end:
        return pos
    mid = (start + end) // 2
    k = lst[mid]
    if k == target:
        if flag:
            return binary_search(lst, target, mid + 1, end, mid, flag)
        else:
            return binary_search(lst, target, start, mid - 1, mid, flag)
    elif k < target:
        return binary_search(lst, target, mid + 1, end, pos, flag)
    else:
        return binary_search(lst, target, start, mid - 1, pos, flag)

n, x = map(int, input().split())
arr = list(map(int, input().split()))
max_idx = binary_search(arr, x, 0, n - 1, -1, True)
min_idx = binary_search(arr, x, 0, n - 1, n, False)
cnt = max_idx - min_idx + 1
if cnt < 0:
    print(-1)
else:
    print(cnt)