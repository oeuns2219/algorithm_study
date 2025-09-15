def find_max(a, b, cs):
    global paper
    global total
    for i in cs:
        summation = 0
        if i == 0:
            summation = sum(paper[a][b:b + 4])
        elif i == 1:
            for j in range(4):
                summation += paper[a + j][b]
        elif i == 2:
            summation += paper[a][b]
            summation += paper[a + 1][b]
            summation += paper[a][b + 1]
            summation += paper[a + 1][b + 1]
        elif i == 3:
            summation += paper[a][b + 1]
            summation += paper[a + 1][b + 1]
            summation += paper[a + 2][b + 1]
            summation += paper[a + 2][b]
        elif i == 4:
            summation += paper[a][b]
            summation += paper[a + 1][b]
            summation += paper[a + 2][b]
            summation += paper[a + 2][b + 1]
        elif i == 5:
            summation += paper[a][b + 1]
            summation += paper[a + 1][b + 1]
            summation += paper[a + 2][b + 1]
            summation += paper[a][b]
        elif i == 6:
            summation += paper[a][b]
            summation += paper[a + 1][b]
            summation += paper[a + 2][b]
            summation += paper[a][b + 1]
        elif i == 7:
            summation += paper[a + 1][b]
            summation += paper[a + 1][b + 1]
            summation += paper[a + 1][b + 2]
            summation += paper[a][b]
        elif i == 8:
            summation += paper[a][b]
            summation += paper[a][b + 1]
            summation += paper[a][b + 2]
            summation += paper[a + 1][b]
        elif i == 9:
            summation += paper[a + 1][b]
            summation += paper[a + 1][b + 1]
            summation += paper[a + 1][b + 2]
            summation += paper[a][b + 2]
        elif i == 10:
            summation += paper[a][b]
            summation += paper[a][b + 1]
            summation += paper[a][b + 2]
            summation += paper[a + 1][b + 2]
        elif i == 11:
            summation += paper[a][b]
            summation += paper[a + 1][b]
            summation += paper[a + 1][b + 1]
            summation += paper[a + 2][b + 1]
        elif i == 12:
            summation += paper[a][b + 1]
            summation += paper[a + 1][b + 1]
            summation += paper[a + 1][b]
            summation += paper[a + 2][b]
        elif i == 13:
            summation += paper[a][b]
            summation += paper[a][b + 1]
            summation += paper[a + 1][b + 1]
            summation += paper[a + 1][b + 2]
        elif i == 14:
            summation += paper[a + 1][b]
            summation += paper[a + 1][b + 1]
            summation += paper[a][b + 1]
            summation += paper[a][b + 2]
        elif i == 15:
            summation += paper[a][b + 1]
            summation += paper[a + 1][b + 1]
            summation += paper[a + 2][b + 1]
            summation += paper[a + 1][b]
        elif i == 16:
            summation += paper[a + 1][b]
            summation += paper[a + 1][b + 1]
            summation += paper[a + 1][b + 2]
            summation += paper[a][b + 1]
        elif i == 17:
            summation += paper[a][b]
            summation += paper[a + 1][b]
            summation += paper[a + 2][b]
            summation += paper[a + 1][b + 1]
        elif i == 18:
            summation += paper[a][b]
            summation += paper[a][b + 1]
            summation += paper[a][b + 2]
            summation += paper[a + 1][b + 1]
        total = max(total, summation)

n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

st = set(range(19))
total = 0
for x in range(n):
    for y in range(m):
        cst = st.copy()
        if x + 1 >= n:
            cst = {0}
        elif x + 2 >= n:
            cst = cst.difference({1, 3, 4, 5, 6, 11, 12, 15, 17})
        elif x + 3 >= n :
            cst = cst.difference({1})

        if y + 1 >= m:
            cst = cst.intersection({1})
        elif y + 2 >= m:
            cst = cst.difference({0, 7, 8, 9, 10, 13, 14, 16, 18})
        elif y + 3 >= m:
            cst = cst.difference({0})

        find_max(x, y, cst)
print(total)