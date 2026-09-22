#완전범죄

def solution(info, n, m):
    info2 = [[abs(a - b), a, b] for a, b in info]
    x = 0
    y = 0
    info2.sort()
    x_lst = []
    while info2:
        _, a, b = info2.pop()
        if a < b and x + a < n:
            x += a
            x_lst.append([a, -b])
        elif b < a and y + b < m:
            y += b
        else:
            if y + b < m:
                y += b
            elif x + a < n:
                x += a
                x_lst.append([a, -b])
            else:
                return -1
    x_lst.sort()
    while x_lst:
        a, b = x_lst.pop()
        if y - b < m:
            x -= a
            y -= b

    return x