from bisect import bisect_left, bisect_right

cnt = 0
target = int(input())
M, N = map(int, input().split())
A = []
B = []
for _ in range(M):
    A.append(int(input()))
for _ in range(N):
    B.append(int(input()))

pa = [0]
pb = []
for idx in range(M):
    total = 0
    for size in range(M - 1):
        total += A[(idx + size) % M]
        pa.append(total)
total = sum(A)
pa.append(total)
for idx in range(N):
    total = 0
    for size in range(N - 1):
        total += B[(idx + size) % N]
        pb.append(total)
total = sum(B)
pb.append(total)
pa.sort()
pb.sort()
left_idx_a = bisect_left(pa, target)
right_idx_a = bisect_right(pa, target)
cnt += right_idx_a - left_idx_a
for idx in range(left_idx_a):
    b_target = target - pa[idx]
    left_idx_b = bisect_left(pb, b_target)
    right_idx_b = bisect_right(pb, b_target)
    cnt += right_idx_b - left_idx_b
print(cnt)