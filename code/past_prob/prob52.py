H, W, X, Y = map(int, input().split())
B = []
for _ in range(H + X):
    B.append(list(map(int, input().split())))

A = [[-1] * W for _ in range(H)]

idx = 0
while idx < H and idx < W:
    x = idx
    for dy in range(W - idx):
        y = idx + dy
        if x < X or y < Y:
            A[x][y] = B[x][y]
        else:
            A[x][y] = B[x][y] - A[x - X][y - Y]
    y = idx
    for dx in range(H - idx - 1):
        x = idx + dx + 1
        if x < X or y < Y:
            A[x][y] = B[x][y]
        else:
            A[x][y] = B[x][y] - A[x - X][y - Y]
    idx += 1

for x in range(H):
    for y in range(W):
        print(A[x][y], end=' ')
    print('')