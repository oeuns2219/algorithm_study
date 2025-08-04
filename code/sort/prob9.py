n = int(input())
lst = list(map(int, input().split()))
lst.sort()
total = 0
for time in lst:
    total += time * n
    n -= 1
print(total)