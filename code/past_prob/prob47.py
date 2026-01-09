INF = int(1e9)

def max_min(eq):
    n = len(eq)
    if n == 1:
        return int(eq), int(eq)
    else:
        max_val = -INF
        min_val = INF
        idx = 1
        while idx < n:
            front = max_min(eq[:idx])
            back = max_min(eq[idx + 1:])
            if eq[idx] == '+':
                new_max = front[0] + back[0]
                new_min = front[1] + back[1]
            elif eq[idx] == '-':
                new_max = front[0] - back[1]
                new_min = front[1] - back[0]
            else:
                lst = [front[0] * back[0], front[0] * back[1], front[1] * back[0], front[1] * back[1]]
                new_max = max(lst)
                new_min = min(lst)
            max_val = max(max_val, new_max)
            min_val = min(min_val, new_min)
            idx += 2
        return max_val, min_val

N = int(input())
equation = input()
result = max_min(equation)
print(result[0])