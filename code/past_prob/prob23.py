r, c, k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))
n = 3
m = 3
T = 0
while T < 100:
    if r <= n and c <= m and A[r - 1][c - 1] == k:
        break
    T += 1
    if n >= m:
        if m > 100:
            n = 100
            m = 100
        new_m = m
        for i in range(n):
            cnt = [0] * 101
            cnt_row = []
            row = []
            for j in range(m):
                cnt[A[i][j]] += 1
            for l in range(1, 101):
                if cnt[l] != 0:
                    cnt_row.append((cnt[l], l))
            cnt_row.sort()
            for e in cnt_row:
                row.append(e[1])
                row.append(e[0])
            new_m = max(new_m, len(row))
            A[i] = row
        for i in range(n):
            if len(A[i]) < new_m:
                for _ in range(new_m - len(A[i])):
                    A[i].append(0)
        m = new_m
    else:
        if n > 100:
            n = 100
            m = 100
        new_n = n
        for j in range(m):
            cnt = [0] * 101
            cnt_col = []
            col = []
            for i in range(n):
                cnt[A[i][j]] += 1
            for l in range(1, 101):
                if cnt[l] != 0:
                    cnt_col.append((cnt[l], l))
            cnt_col.sort()
            for e in cnt_col:
                col.append(e[1])
                col.append(e[0])
            if new_n < len(col):
                for _ in range(len(col) - new_n):
                    A.append([0] * m)
                new_n = len(col)
            for i in range(len(col)):
                A[i][j] = col[i]
            for i in range(len(col), new_n):
                A[i][j] = 0
        n = new_n
if T == 100:
    if r <= n and c <= m and A[r - 1][c - 1] == k:
        print(T)
    else:
        print(-1)
else:
    print(T)