
def is_right(string):
    left_cnt = 0
    right_cnt = 0
    idx = 0
    res = True
    for i in range(len(string)):
        c = string[i]
        if c == '(':
            left_cnt += 1
        else:
            right_cnt += 1

        if right_cnt > left_cnt:
            res = False

        if idx == 0 and left_cnt == right_cnt:
            idx = i

        if not res and idx:
            break

    return idx, res

def solution(p):
    idx, right = is_right(p)

    if right:
        return p
    else:
        u = p[:idx + 1]
        v = p[idx + 1:]
        idx, right = is_right(u)
        if right:
            return u + solution(v)
        else:
            new_u = u[1:-1]
            new_u = new_u.replace('(', '*')
            new_u = new_u.replace(')', '(')
            new_u = new_u.replace('*', ')')
            return '(' + solution(v) + ')' + new_u

