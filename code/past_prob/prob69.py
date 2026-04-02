N = int(input())
switches = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    sex, num = map(int, input().split())
    if sex == 1:
        i = 1
        while num * i <= N:
            switches[(num * i) - 1] += 1
            switches[(num * i) - 1] %= 2
            i += 1
    else:
        start = num
        end = num
        while switches[start - 1] == switches[end - 1]:
            switches[start - 1] += 1
            switches[start - 1] %= 2
            if start != end:
                switches[end - 1] += 1
                switches[end - 1] %= 2
            if start - 1 > 0 and end + 1 <= N:
                start -= 1
                end += 1
                continue
            break

for i in range(N // 20):
    for j in range(20):
        print(switches[(20 * i) + j], end = ' ')
    print('')
idx = N - (N % 20)
for i in range(idx, N):
    print(switches[i], end = ' ')