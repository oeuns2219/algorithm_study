def operate(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        if a < 0:
            return -((-a) // b)
        else:
            return a // b

def calc(idx, ops, total):
    global n
    global ans
    global min_total
    global max_total
    if idx == n:
        min_total = min(min_total, total)
        max_total = max(max_total, total)
    else:
        for i in range(4):
            if ops[i] != 0:
                ops[i] -= 1
                new_total = operate(total, ans[idx], i)
                calc(idx + 1, ops, new_total)
                ops[i] += 1

n = int(input())
ans = list(map(int, input().split()))
oper = list(map(int, input().split()))
min_total = int(1e9)
max_total = -int(1e9)
calc(1, oper, ans[0])
print(max_total)
print(min_total)