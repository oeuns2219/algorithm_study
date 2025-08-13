n = int(input())
soldier_lst = list(map(int, input().split()))
max_cnt = [1] * n

for i in range(n):
    for j in range(i):
        if soldier_lst[i] < soldier_lst[j]:
            max_cnt[i] = max((max_cnt[i], max_cnt[j] + 1))

print(n - max(max_cnt))