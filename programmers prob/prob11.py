#아방가르드 타일링

def solution(n):
    mod = int(1e9) + 7
    cnt_lst = [1]

    for i in range(1, n + 1):
        res = 0
        if i < 6:
            for j in range(1, i + 1):
                part = cnt_lst[i - j]
                if j == 1:
                    res += part
                elif j == 3:
                    res += part * 5
                else:
                    if j % 3 == 0:
                        res += part * 4
                    else:
                        res += part * 2
        else:
            res += cnt_lst[i - 1] + 2 * cnt_lst[i - 2] + 6 * cnt_lst[i - 3] + cnt_lst[i - 4] - cnt_lst[i - 6]
        cnt_lst.append(res)
    return cnt_lst[n] % mod