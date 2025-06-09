n, m = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        if lst[i] != lst[j]: cnt += 1

print(cnt)