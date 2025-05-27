n, k = map(int, input().split())
cnt = n % k
n -= cnt

while n != 0:
    if n // k > 0:
        n = n // k
        cnt += 1
    rest = n % k
    cnt += rest
    n -= rest

print(cnt - 1)
