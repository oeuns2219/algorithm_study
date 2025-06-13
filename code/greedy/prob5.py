str = input()
res = int(str[0])

for i in str[1:]:
    cur = int(i)
    if res <= 1 or cur <= 1: res += cur
    else: res *= cur
print(res)