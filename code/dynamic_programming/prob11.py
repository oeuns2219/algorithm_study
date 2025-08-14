t = int(input())
fibo = [(1, 0), (0, 1)]
for i in range(2, 41):
    f_1 = fibo[i - 1]
    f_2 = fibo[i - 2]
    fibo.append((f_1[0] + f_2[0], f_1[1] + f_2[1]))
for _ in range(t):
    n = int(input())
    print(fibo[n][0], fibo[n][1])
