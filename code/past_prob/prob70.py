from collections import deque

N = int(input())
M = int(input())
friendship = [[] for _ in range(N)]
enemy = [[] for _ in range(N)]
for _ in range(M):
    relation, s1, s2 = input().split()
    n1, n2 = int(s1), int(s2)
    if relation == 'F':
        friendship[n1 - 1].append(n2 - 1)
        friendship[n2 - 1].append(n1 - 1)
    else:
        enemy[n1 - 1].append(n2 - 1)
        enemy[n2 - 1].append(n1 - 1)

for i in range(N):
    for e in enemy[i]:
        for j in enemy[e]:
            if i != j and not j in friendship[i]:
                friendship[i].append(j)

visited = [False] * N
cnt = 0
for i in range(N):
    if not visited[i]:
        cnt += 1
        q = deque([i])
        visited[i] = True
        while q:
            c = q.popleft()
            for f in friendship[c]:
                if not visited[f]:
                    q.append(f)
                    visited[f] = True
print(cnt)