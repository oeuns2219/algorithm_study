
lst = []
for _ in range(9):
    lst.append(int(input()))
total = 0
flag = False
idx_lst = []
for a in range(3):
    total += lst[a]
    for b in range(a + 1, 4):
        total += lst[b]
        for c in range(b + 1, 5):
            total += lst[c]
            for d in range(c + 1, 6):
                total += lst[d]
                for e in range(d + 1, 7):
                    total += lst[e]
                    for f in range(e + 1, 8):
                        total += lst[f]
                        for g in range(f + 1, 9):
                            total += lst[g]
                            if total == 100:
                                idx_lst.append(g)
                                flag = True
                                break
                            total -= lst[g]
                        if flag:
                            idx_lst.append(f)
                            break
                        total -= lst[f]
                    if flag:
                        idx_lst.append(e)
                        break
                    total -= lst[e]
                if flag:
                    idx_lst.append(d)
                    break
                total -= lst[d]
            if flag:
                idx_lst.append(c)
                break
            total -= lst[c]
        if flag:
            idx_lst.append(b)
            break
        total -= lst[b]
    if flag:
        idx_lst.append(a)
        break
    total -= lst[a]

height_lst = [lst[e] for e in idx_lst]
height_lst.sort()
for height in height_lst:
    print(height)