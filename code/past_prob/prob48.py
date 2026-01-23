import heapq

INF = int(1e9)

def is_possible(v):
    global N
    global K
    global INF
    global cables
    min_length = [INF] * N
    min_length[0] = 0
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        cur_cost, cur_node = heapq.heappop(q)
        if cur_cost > min_length[cur_node]:
            continue

        for new_node, new_v in cables[cur_node]:
            new_cost = cur_cost
            if new_v > v:
                new_cost += 1

            if new_cost < min_length[new_node]:
                min_length[new_node] = new_cost
                heapq.heappush(q, (new_cost, new_node))

    if min_length[N - 1] <= K:
        return True
    else:
        return False

N, P, K = map(int, input().split())
cables = [[] for _ in range(N)]
for _ in range(P):
    x, y, cost = map(int, input().split())
    cables[x - 1].append((y - 1, cost))
    cables[y - 1].append((x - 1, cost))

if not is_possible(1e6):
    print(-1)
elif is_possible(0):
    print(0)
else:
    start = 1
    end = int(1e6)
    while start <= end:
        mid = (start + end) // 2
        if is_possible(mid):
            end = mid - 1
        else:
            start = mid + 1
    print(start)