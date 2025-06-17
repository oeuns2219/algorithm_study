n = int(input())
lst = list(input().split())
x = 1
y = 1

for d in lst:
    if d == 'L' and y != 1:
        y -= 1
    elif d == 'R' and y != n:
        y += 1
    elif d == 'U' and x != 1:
        x -= 1
    elif d == 'D' and x != n:
        x += 1

print(x, y)