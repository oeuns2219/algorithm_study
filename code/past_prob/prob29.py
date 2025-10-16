max_score = 0

def move(g, p, d, s, total):
    global max_score
    if len(d) == 0:
        max_score = max(max_score, total)
    else:
        num = d.pop()
        for e in range(4):
            if p[e] != 21:
                prev = p[e]
                cur = prev
                if len(g[cur]) == 2:
                    cur = g[cur][1]
                else:
                    cur = g[cur][0]
                for _ in range(num - 1):
                    if cur != 21:
                        cur = g[cur][0]
                    else:
                        break
                if cur == 21 or not cur in p:
                    p[e] = cur
                    move(g, p, d, s, total + s[cur])
                    p[e] = prev
        d.append(num)

score = [0] * 33
graph = [[] for _ in range(33)]
for i in range(21):
    graph[i].append(i + 1)
    score[i] = 2 * i
graph[5].append(22)
graph[22].append(23)
graph[23].append(24)
graph[24].append(30)
for i in range(3):
    score[22 + i] = 13 + (3 * i)
graph[10].append(25)
graph[25].append(26)
graph[26].append(30)
for i in range(2):
    score[25 + i] = 22 + (2 * i)
graph[15].append(27)
for i in range(4):
    graph[27 + i].append(27 + i + 1)
    score[27 + i] = 28 - i
graph[30].append(31)
graph[31].append(32)
graph[32].append(20)
for i in range(2):
    score[31 + i] = 30 + (5 * i)

pos = [0] * 4
dice = list(map(int, input().split()))
dice.reverse()
move(graph, pos, dice, score, 0)
print(max_score)