#선인장 숨기기
#슬라이딩 윈도우 알고리즘 사용

from collections import deque

def solution(m, n, h, w, drops):
    unrained = len(drops) + 1
    r = m - h + 1
    s = n - w + 1
    desert = [[unrained] * n for _ in range(m)]
    desert2 = [[] for _ in range(r)]
    max_x = -1
    max_y = -1
    max_t = 0
    for t in range(len(drops)):
        desert[drops[t][0]][drops[t][1]] = t + 1

    for oy in range(n):
        q = deque([0])
        for ox in range(1, h - 1):
            while q and desert[q[-1]][oy] >= desert[ox][oy]:
                q.pop()
            q.append(ox)
        for ox in range(h - 1, m):
            if q[0] <= ox - h:
                q.popleft()
            while q and desert[q[-1]][oy] >= desert[ox][oy]:
                q.pop()
            q.append(ox)
            desert2[ox - h + 1].append(desert[q[0]][oy])

    for ox in range(r):
        q = deque([0])
        for oy in range(1, w - 1):
            while q and desert2[ox][q[-1]] >= desert2[ox][oy]:
                q.pop()
            q.append(oy)
        for oy in range(w - 1, n):
            if q[0] <= oy - w:
                q.popleft()
            while q and desert2[ox][q[-1]] >= desert2[ox][oy]:
                q.pop()
            q.append(oy)
            min_t = desert2[ox][q[0]]
            if min_t > max_t:
                max_t = min_t
                max_x = ox
                max_y = oy - w + 1

    return [max_x, max_y]