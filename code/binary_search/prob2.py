def binary_search(lst, target, start, end, max_height):
    if start > end:
         return max_height
    mid = (start + end) // 2
    height = lst[mid]
    new_lst = [e - height for e in lst if e > height]
    if sum(new_lst) >= target:
        return binary_search(lst, target, mid + 1, end, height)
    else:
        return binary_search(lst, target, start, mid - 1, max_height)


n, m = map(int, input().split())
len_lst = list(map(int, input().split()))
len_lst.sort()
mh = binary_search(len_lst, m, 0, n - 1, 0)

while True:
    nmh = mh + 1
    new_len_lst = [e - nmh for e in len_lst if e > nmh]
    if sum(new_len_lst) < m:
        break
    mh = nmh
print(mh)