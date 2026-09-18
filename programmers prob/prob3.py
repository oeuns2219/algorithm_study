# 빛의 경로 사이클
# 북, 동, 남, 서

def length(grid, visited, crossed, x, y, di):
    direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    lth = 0

    while not crossed[x][y][di]:
        lth += 1
        crossed[x][y][di] = True
        if sum(crossed[x][y]) == 4:
            visited[x][y] = True
        dx, dy = direct[di]
        nx, ny = x + dx, y + dy
        if nx < 0:
            nx = len(grid) - 1
        elif nx >= len(grid):
            nx = 0
        if ny < 0:
            ny = len(grid[0]) - 1
        elif ny >= len(grid[0]):
            ny = 0
        if grid[nx][ny] == 'L':
            di = (di - 1) % 4
        elif grid[nx][ny] == 'R':
            di = (di + 1) % 4
        x, y = nx, ny

    return lth

def solution(grid):
    crossed = [[[False] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    answer = []

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if not visited[x][y]:
                for i in range(4):
                    if not crossed[x][y][i]:
                        answer.append(length(grid, visited, crossed, x, y, i))
    answer.sort()

    return answer

print(solution(["S"]))