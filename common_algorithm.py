from collections import deque
from heapq import heappop, heappush

from code.graph.prob9 import indegree

INF = int(1e9)

def dfs(graph, start, visited):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True

def binary_search(graph, start, end, target, is_left):
    while start <= end:
        mid = (start + end) // 2

        if target < graph[mid]:
            end = mid - 1
        elif target == graph[mid]:
            if is_left:
                end = mid - 1
            else:
                start = mid + 1
        else:
            start = mid + 1
    return start

def dijkstra(graph, start):
    min_lst = [INF] * len(graph)
    min_lst[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        cur_cost, cur_node = heappop(q)
        if cur_cost > min_lst[cur_node]:
            continue

        for next_node, cost in graph[cur_node]:
            new_cost = cur_cost + cost
            if new_cost < min_lst[next_node]:
                min_lst[next_node] = new_cost
                heappush(q, (new_cost, next_node))
    return min_lst

def floyd_warshall(graph):
    min_lst = [[INF] * len(graph) for _ in range(len(graph))]
    for i in range(len(graph)):
        min_lst[i][i] = 0
        for j, cost in graph[i]:
            min_lst[i][j] = cost

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                min_lst[i][j] = min(min_lst[i][j], graph[i][k] + graph[k][j])
    return min_lst

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    px = find_parent(parent, x)
    py = find_parent(parent, y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

def kruskal(edges, parent):
    edges.sort()
    res = 0
    for cost, node1, node2 in edges:
        p1 = find_parent(parent, node1)
        p2 = find_parent(parent, node2)
        if p1 != p2:
            union(parent, node1, node2)
            res += cost
    return res

def topological_sort(graph):
    indegree = [0] * len(graph)
    q = deque()
    res = []

    for lst in graph:
        for node in lst:
            indegree[node] += 1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        res.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    return res