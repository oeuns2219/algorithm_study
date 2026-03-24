
def find_root(p, i, idx):
    pos = i.index(p[0])
    if pos != 0:
        find_root(p[1:], i[:pos], (idx * 2) + 1)
    if len(i[pos + 1:]) != 0:
        find_root(p[pos + 1:], i[pos + 1:], (idx * 2) + 2)
    print(p[0], end=' ')

T = int(input())
for _ in range(T):
    N = int(input())
    pre = list(map(int, input().split()))
    ino = list(map(int, input().split()))
    find_root(pre, ino, 0)
    print('')