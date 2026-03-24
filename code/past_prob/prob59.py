N, W, L = map(int ,input().split())
weight = list(map(int, input().split()))

start = 0
end = 0
T = 1
bridge = [0] * W
bridge[-1] = weight[0]
while True:
    if bridge[0] != 0:
        start += 1
    if end == N - 1:
        bridge.reverse()
        idx = bridge.index(weight[end])
        T += W - idx
        break
    if sum(bridge[1:]) + weight[end + 1] <= L:
        end += 1
    else:
        idx = bridge.index(weight[start], 1)
        T += idx
        bridge = bridge[idx:] + ([0] * idx)
        continue
    bridge = bridge[1:] + [weight[end]]
    T += 1

print(T)