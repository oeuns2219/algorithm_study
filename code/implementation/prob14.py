T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    target = [0] * n
    target[m] = 1
    cnt = 1
    cur = 0
    while len(priority) != 0:
        if priority[cur] != max(priority):
            cur += 1
        else:
            if target[cur]:
                print(cnt)
                break
            else:
                cnt += 1
                priority.pop(cur)
                target.pop(cur)

        if cur == len(priority):
            cur = 0
