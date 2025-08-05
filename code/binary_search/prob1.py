def binary_search(lst, target, start, end):
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] > target:
            return binary_search(lst, target, start, mid - 1)
        else:
            return binary_search(lst, target, mid + 1, end)

n = int(input())
part_lst = list(map(int, input().split()))
part_lst.sort()
m = int(input())
order_lst = list(map(int, input().split()))


for part in order_lst:
    if binary_search(part_lst, part, 0, n - 1):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')