
N, K = map(int, input().split())
slots = list(map(int, input().split()))
robot = []
t = 1
while True:
    for i in range(len(robot)):
        robot[i] += 1
    slots = [slots[-1]] + slots[:-1]
    if len(robot) != 0 and robot[0] == N - 1:
        robot.pop(0)
    for i in range(len(robot)):
        if (i == 0 or robot[i - 1] != robot[i] + 1) and slots[robot[i] + 1] > 0:
            slots[robot[i] + 1] -= 1
            robot[i] += 1
    if len(robot) != 0 and robot[0] == N - 1:
        robot.pop(0)
    if slots[0] > 0:
        slots[0] -= 1
        robot.append(0)
    cnt = 0
    for e in slots:
        if e == 0:
            cnt += 1
    if cnt >= K:
        break
    t += 1
print(t)
