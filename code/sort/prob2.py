n = int(input())
data = []
for _ in range(n):
    a, b = input().split()
    b = int(b)
    data.append((b, a))
data = sorted(data)
for _, name in data:
    print(name, end=' ')
