n = int(input())
min_cnt = [0]

for idx in range(1, n):
    num = idx + 1
    lst = [min_cnt[idx - 1]]
    if num % 3 == 0:
        lst.append(min_cnt[(num // 3) - 1])
    if num % 2 == 0:
        lst.append(min_cnt[(num // 2) - 1])
    min_cnt.append(1 + min(lst))
print(min_cnt[n - 1])