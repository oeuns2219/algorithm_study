def dfs(g, v, ns, s, d, c):
    while len(s) != 0:
        k = s[-1]
        cnt, i = d[-1]
        exist = False
        for j in range(i, len(g[k])):
            node = g[k][j]
            if not v[node]:
                v[node] = True
                d[-1][1] = j + 1
                s.append(node)
                d.append([1, 0])
                exist = True
                break
            else:
                if node in s:
                    i = s.index(node)
                    c.append(set(s[i:] + [node]))
                else:
                    cnt += ns[node]
        if exist:
            continue
        else:
            s.pop()
            d.pop()
            ns[k] = cnt
            if len(s) != 0:
                d[-1][0] += cnt

def cycle_resolution(c, ns):
    i = 0
    while i < len(c):
        l = len(c)
        del_lst =[]
        for j in range(i + 1, l):
            if len(c[i].intersection(c[j])) != 0:
                c[i] = c[i].union(c[j])
                del_lst.append(j)
        del_lst.sort(reverse=True)
        for j in del_lst:
            c.pop(j)
        i += 1

    for cy in c:
        max_val = 0
        for j in cy:
            max_val = max((max_val, ns[j]))
        for j in cy:
            ns[j] = max_val

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

nums = [0] * (n + 1)
visited = [False] * (n + 1)
cycle = []
for com in range(1, n+1):
    if not visited[com]:
        visited[com] = True
        dfs(graph, visited, nums, [com], [[1, 0]], cycle)

cycle_resolution(cycle, nums)

max_num = max(nums)
while nums.count(max_num) != 0:
    idx = nums.index(max_num)
    print(idx, end=' ')
    nums[idx] = 0