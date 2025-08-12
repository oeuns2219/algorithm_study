n = int(input())
schedule = []
max_profit = [0] * (n + 1)
for _ in range(n):
    schedule.append(tuple(map(int, input().split())))
for i in range(n-1, -1, -1):
    if schedule[i][0] == 1:
        max_profit[i] = max_profit[i + 1] + schedule[i][1]
    elif i + schedule[i][0] > n:
        max_profit[i] = max_profit[i + 1]
    else:
        max_profit[i] = max((max_profit[i + schedule[i][0]] + schedule[i][1], max_profit[i + 1]))
print(max_profit[0])