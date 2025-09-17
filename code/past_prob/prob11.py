def make_team(ns, team):
    global n
    global s
    global diff
    if len(team) == n / 2:
        total1 = 0
        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                total1 += s[team[i] - 1][team[j] - 1]
                total1 += s[team[j] - 1][team[i] - 1]
        total2 = 0
        for i in range(1, n + 1):
            if ns[i]:
                for j in range(i + 1, n + 1):
                    if ns[j]:
                        total2 += s[i - 1][j - 1]
                        total2 += s[j - 1][i - 1]
        diff = min(diff, abs(total1 - total2))
    else:
        if team:
            start = team[-1]
        else:
            start = 0
        for i in range(start + 1, n + 1):
            if ns[i]:
                ns[i] = False
                make_team(ns, team + [i])
                ns[i] = True

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
nums = [[True] for _ in range(n + 1)]
diff = 100
make_team(nums, [])
print(diff)