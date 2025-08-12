n = int(input())
upper = [int(input())]
for i in range(1, n):
    before = list(map(int, input().split()))
    after = [0] * (i + 1)
    for j in range(i + 1):
        if j == 0:
            after[j] = before[j] + upper[j]
        elif j == i:
            after[j] = before[j] + upper[j - 1]
        else:
            after[j] = before[j] + max((upper[j], upper[j - 1]))
    upper = after
print(max(upper))