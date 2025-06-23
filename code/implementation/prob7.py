s = input()
n = len(s)
res = None

for i in range(1, (n//2)+1):
    s_lst = []
    rep = False
    before = None
    for j in range(n // i):
        part = s[i*j:i*(j+1)]
        if not(before is None) and part == before:
            rep = True
        elif before is None:
            before = part
        else:
            if rep:
                s_lst.append('1' + before)
                rep = False
            else:
                s_lst.append(before)
            before = part

    if rep:
        s_lst.append('1' + before)
    else:
        s_lst.append(before)
    s_lst.append(s[i * (n//i):])
    m = len(''.join(s_lst))
    if res is None: res = m
    else:
        if m < res: res = m

print(res)