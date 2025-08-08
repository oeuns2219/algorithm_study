def binary_search(arr, start, end, first, pair):
    if start > end:
        return pair
    mid = (start + end) // 2
    second = arr[mid]
    mix = first + second
    if first != second and abs(mix) < pair[0]:
        pair = (abs(mix), first, second)

    if mix == 0:
        return pair
    elif mix > 0:
        return binary_search(arr, start, mid - 1, first, pair)
    else:
        return binary_search(arr, mid + 1, end, first, pair)


n = int(input())
lst = list(map(int, input().split()))
lst.sort()
mixture = []
for liquid in lst:
    mixture.append(binary_search(lst, 0, n - 1, liquid, (2 * int(1e9),0, 0)))
mixture.sort()
res = list((mixture[0][1], mixture[0][2]))
res.sort()
print(res[0], res[1])