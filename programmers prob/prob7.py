#3 x n 타일링

def solution(n):
    lst = [3, 11]
    i = 2

    while 2 * len(lst) < n:
        lst.append(4 * lst[-1] - lst[-2])

    return lst[n // 2 - 1] % int(1e9 + 7)
