count = [0] * 100000
n = int(input())
for _ in range(n):
    k = int(input())
    count[k-1] += 1
for i in range(len(count)-1, -1, -1):
    for _ in range(count[i]):
        print(i + 1, end=' ')