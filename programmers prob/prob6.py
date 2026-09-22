#도넛과 막대 그래프

from collections import deque

def solution(edges):
    answer = [0, 0, 0, 0]
    size = max(map(max, edges))
    indegree = dict()
    graph = dict()
    visited = dict()
    stick = []

    for a, b in edges:
        if a - 1 in graph:
            graph[a - 1].append(b - 1)
        else:
            graph[a - 1] = [b - 1]
        if not b - 1 in graph:
            graph[b - 1] = []

        if b - 1 in indegree:
            indegree[b - 1] += 1
        else:
            indegree[b - 1] = 1
        if not a - 1 in indegree:
            indegree[a - 1] = 0

        if not a - 1 in visited:
            visited[a - 1] = False
        if not b - 1 in visited:
            visited[b - 1] = False

    for i in graph.keys():
        if len(graph[i]) >= 2 and indegree[i] == 0:
            answer[0] += i + 1
            visited[i] = True
            indegree[i] -= 1
            while graph[i]:
                node = graph[i].pop()
                indegree[node] -= 1
            break

    for i in graph.keys():
        if indegree[i] == 0:
            stick.append(i)
    answer[2] += len(stick)
    while stick:
        node = stick.pop()
        visited[node] = True
        while graph[node]:
            node = graph[node].pop()
            visited[node] = True

    for i in graph.keys():
        if not visited[i]:
            is_eight = False
            q = deque([i])
            while q:
                cur = q.popleft()
                if len(graph[cur]) == 2:
                    is_eight = True
                while graph[cur]:
                    new = graph[cur].pop()
                    visited[new] = True
                    q.append(new)
            if is_eight:
                answer[3] += 1
            else:
                answer[1] += 1

    return answer

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))