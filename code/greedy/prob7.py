n = int(input())
lst = list(map(int, input().split()))
rset = set()

def find_val(i, v):
    global lst
    global n
    if i <= n:
        for j in range(i, n):
            nv = v + lst[j]
            rset.add(nv)
            find_val(j+1, nv)

find_val(0, 0)

res = 1

while True:
    if not (res in rset): break
    else: res += 1

print(res)