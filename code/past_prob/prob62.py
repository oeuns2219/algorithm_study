T = int(input())
for _ in range(T):
    N = int(input())
    blocked = [[[-1, -1] for _ in range(2)] for _ in range(N)]
    paper = list(map(int, input().split()))
    res = True
    for i in range(N - 1):
        a, b = paper[i] - 1, paper[i + 1] - 1
        max_val, min_val = max(a, b), min(a, b)
        left_max, left_min = max(blocked[a][0]), min(blocked[a][0])
        right_max, right_min = max(blocked[a][1]), min(blocked[a][1])
        if left_max == -1 or (left_max > a > left_min and left_max > b > left_min) or (max_val > left_max > min_val and max_val > left_min > min_val):
            for j in range(min_val, max_val + 1):
                left_max, left_min = max(blocked[j][0]), min(blocked[j][0])
                if left_max == -1 or (left_max > a > left_min and left_max > b > left_min):
                    blocked[j][0] = [a, b]
                elif max_val > left_max > min_val and max_val > left_min > min_val:
                    continue
                else:
                    res = False
                    break
        elif right_max == -1 or (right_max > a > right_min and right_max > b > right_min) or (max_val > right_max > min_val and max_val > right_min > min_val):
            for j in range(min_val, max_val + 1):
                if right_max == -1 or (right_max > a > right_min and right_max > b > right_min):
                    blocked[j][1] = [a, b]
                elif max_val > right_max > min_val and max_val > right_min > min_val:
                    continue
                else:
                    res = False
                    break
        else:
            res = False

        if not res:
            break

    if res:
        print('YES')
    else:
        print('NO')