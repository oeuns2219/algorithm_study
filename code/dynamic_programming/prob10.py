a = input()
b = input()
n = len(a)
m = len(b)
edit_dist = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    edit_dist[i][0] = i

for j in range(1, m + 1):
    edit_dist[0][j] = j

for k in range(1, n + 1):
    for l in range(1, m + 1):
        if a[k - 1] == b[l - 1]:
            edit_dist[k][l] = edit_dist[k - 1][l - 1]
        else:
            edit_dist[k][l] = 1 + min((edit_dist[k - 1][l - 1], edit_dist[k - 1][l], edit_dist[k][l - 1]))

print(edit_dist[n][m])