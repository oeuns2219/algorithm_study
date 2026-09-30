#최고 속도

import heapq

INF = int(1e9)

def insert_dict(graph, key, elem):
    if key in graph:
        graph[key].append(elem)
    else:
        graph[key] = [elem]

def solution(city, road):
    global INF
    graph = dict()
    limit = dict()
    visited = dict()
    y_line = dict()
    x_line = dict()
    res = []

    for x1, y1, x2, y2, speed in road:
        if y1 == y2:
            insert_dict(y_line, y1, [x1, x2, speed])
        else:
            insert_dict(x_line, x1, [y1, y2, speed])

    for y in y_line:
        lines = y_line[y]
        lines.sort()
        for i in range(len(lines)):
            x1, x2 = lines[i][0], lines[i][1]
            cam = (x1 + x2) // 2
            lst = [cam]
            if not (cam, y) in limit:
                limit[(cam, y)] = lines[i][2]
                visited[(cam, y)] = False
            else:
                limit[(cam, y)] = min(limit[(cam, y)], lines[i][2])
            for cx, cy in city:
                if cy == y and x1 <= cx <= x2:
                    lst.append(cx)
                    if not (cx, y) in limit:
                        limit[(cx, y)] = INF
                        visited[(cx, y)] = False

            if i < len(lines) - 1 and not x2 in lst and x2 == lines[i + 1][0]:
                lst.append(x2)
                if not (x2, y) in limit:
                    limit[(x2, y)] = INF
                    visited[(x2, y)] = False
            if i > 0 and not x1 in lst and x1 == lines[i - 1][1]:
                lst.append(x1)

            for x in x_line:
                if not x in lst and x1 <= x <= x2:
                    contain = False
                    for y1, y2, speed in x_line[x]:
                        if y1 <= y <= y2:
                            contain = True
                            break
                    if contain:
                        lst.append(x)
                        if not (x, y) in limit:
                            limit[(x, y)] = INF
                            visited[(x, y)] = False
            lst.sort()
            for j in range(len(lst) - 1):
                x1, x2 = lst[j], lst[j + 1]
                insert_dict(graph, (x1, y), (x2, y))
                insert_dict(graph, (x2, y), (x1, y))

    for x in x_line:
        lines = x_line[x]
        lines.sort()
        for i in range(len(lines)):
            y1, y2 = lines[i][0], lines[i][1]
            cam = (y1 + y2) // 2
            lst = [cam]
            if not (x, cam) in limit:
                limit[(x, cam)] = lines[i][2]
                visited[(x, cam)] = False
            else:
                limit[(x, cam)] = min(limit[(x, cam)], lines[i][2])
            for cx, cy in city:
                if cx == x and y1 <= cy <= y2:
                    lst.append(cy)
                    if not (x, cy) in limit:
                        limit[(x, cy)] = INF
                        visited[(x, cy)] = False

            if i < len(lines) - 1 and not y2 in lst and y2 == lines[i + 1][0]:
                lst.append(y2)
                if not (x, y2) in limit:
                    limit[(x, y2)] = INF
                    visited[(x, y2)] = False
            if i > 0 and not y1 in lst and y1 == lines[i - 1][1]:
                lst.append(y1)

            for y in y_line:
                if not y in lst and y1 <= y <= y2:
                    contain = False
                    for x1, x2, speed in y_line[y]:
                        if x1 <= x <= x2:
                            contain = True
                            break
                    if contain:
                        lst.append(y)
            lst.sort()
            for j in range(len(lst) - 1):
                y1, y2 = lst[j], lst[j + 1]
                insert_dict(graph, (x, y1), (x, y2))
                insert_dict(graph, (x, y2), (x, y1))

    q = []
    heapq.heappush(q, (-INF, city[0][0], city[0][1]))
    while q:
        minus, cx, cy = heapq.heappop(q)
        cl = -minus
        for nx, ny in graph[(cx, cy)]:
            if not visited[(nx, ny)]:
                visited[(nx, ny)] = True
                limit[(nx, ny)] = min(limit[(nx, ny)], cl)
                heapq.heappush(q, (-limit[(nx, ny)], nx, ny))

    for cx, cy in city[1:]:
        speed = limit[(cx, cy)]
        if speed == INF:
            res.append(0)
        else:
            res.append(speed)
    return res