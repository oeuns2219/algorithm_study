n, m = map(int, input().split())
val_lst = []
for _ in range(n):
    val_lst.append(int(input()))

cnt_lst = [0] * m
for i in range(m):
    val = i + 1
    lst = []
    for j in range(n):
        if val == val_lst[j]:
            lst.append(1)
        elif val > val_lst[j]:
            cnt_remain = cnt_lst[i - val_lst[j]]
            if cnt_remain != -1:
                lst.append(cnt_lst[i - val_lst[j]] + 1)

    if len(lst) == 0:
        cnt_lst[i] = -1
    else:
        cnt_lst[i] = min(lst)

print(cnt_lst[m - 1])
