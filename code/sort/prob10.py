n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()

weight_lst = [lst[i] * (n - i) for i in range(n)]
print(max(weight_lst))