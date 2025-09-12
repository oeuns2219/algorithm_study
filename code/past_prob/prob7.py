n = int(input())
num_lst = list(map(int, input().split()))
b, c = map(int, input().split())
total = n
for num in num_lst:
    if num > b:
        total += (num - b) // c
        if (num - b) % c:
            total += 1
print(total)