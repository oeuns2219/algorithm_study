s = input()
cnt0 = 0
cnt1 = 0
cur = s[0]

for i in s:
    if i != cur:
        cur = i
        if i == '0': cnt1 += 1
        else: cnt0 += 1

if cur == '1': cnt1 += 1
else: cnt0 += 1

print(min((cnt0, cnt1)))