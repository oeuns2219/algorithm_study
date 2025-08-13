n = int(input())
ugly_lst = [1]
cur = 2
while len(ugly_lst) != n:
    if cur % 2 == 0 and (cur / 2) in ugly_lst:
        ugly_lst.append(cur)
    elif cur % 3 == 0 and (cur / 3) in ugly_lst:
        ugly_lst.append(cur)
    elif cur % 5 == 0 and (cur / 5) in ugly_lst:
        ugly_lst.append(cur)
    cur += 1
print(ugly_lst[-1])