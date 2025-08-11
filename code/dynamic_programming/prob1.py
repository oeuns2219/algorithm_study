x = int(input())

cnt_lst = [0]

for i in range(1, x):
    lst = [cnt_lst[i - 1]]
    val = i + 1
    if val % 5 == 0:
        lst.append(cnt_lst[(val // 5) - 1])
    elif val % 3 == 0:
        lst.append(cnt_lst[(val // 3) - 1])
    elif val % 2 == 0:
        lst.append(cnt_lst[(val // 2) - 1])
    cnt_lst.append(min(lst) + 1)

print(cnt_lst[x - 1])