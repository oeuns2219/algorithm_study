T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    yy = ((n - 1) % h) + 1
    xx = ((n - 1) // h) + 1
    print((yy * 100) + xx)