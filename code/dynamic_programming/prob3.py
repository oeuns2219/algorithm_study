n = int(input())
lst = [0] * n
lst[0] = 1
lst[1] = 3
for i in range(2, n):
    lst[i] = (lst[i - 1] + (lst[i - 2] * 2)) % 796796
print(lst[n - 1])
