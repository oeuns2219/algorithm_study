string = input()
alpha_lst = []
cnt = 0
for i in string:
    if i.isalpha(): alpha_lst.append(i)
    else: cnt += int(i)
alpha_lst.sort()
print(''.join(alpha_lst) + str(cnt))