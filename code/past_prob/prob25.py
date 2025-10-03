direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(l, v, x, y):
    global N
    v[x][y] = 0
    q = [(x, y, 0)]
    while q:
        cx, cy, ct = q.pop(0)
        for dx ,dy in direction:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < N and 0 <= ny < N and (l[nx][ny] == 0 or l[nx][ny] == 2) and (v[nx][ny] == -1 or v[nx][ny] > ct + 1):
                v[nx][ny] = ct + 1
                q.append((nx, ny, ct + 1))

def activate_virus(l, vs, act, nact):
    global N
    global M
    global min_time
    if len(act) == M:
        time = [[-1] * N for _ in range(N)]
        for x, y in act:
            bfs(l, time, x, y)
        for x in range(N):
            for y in range(N):
                if l[x][y] == 0 and time[x][y] == -1:
                    return
        for x, y in vs + nact:
            time[x][y] = 0
        min_time = min(min_time, max(map(max, time)))
    else:
        if len(vs) >= M - len(act):
            virus = vs.pop()
            act.append(virus)
            activate_virus(l, vs, act, nact)
            act.pop()
            nact.append(virus)
            activate_virus(l, vs, act, nact)
            nact.pop()
            vs.append(virus)

N, M = map(int, input().split())
viruses = []
lab = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            viruses.append((i, j))
    lab.append(row)

min_time = int(1e9)
activate_virus(lab, viruses, [], [])
if min_time == int(1e9):
    print(-1)
else:
    print(min_time)