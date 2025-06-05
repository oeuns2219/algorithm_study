def less_cnt(l, k):
    cnt = 0
    for i in l:
        if i <= k: cnt += 1
        else: break
    return cnt

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
num = 0
k = lst[0]

while len(lst) != 0:
    if len(lst) < k: break
    else:
        if less_cnt(lst, k) >= k:
            num += 1
            lst = lst[k:]
        else: k += 1

print(num)