def solution(board):
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    h_board = [[-1] * (n+1) for _ in range(n+2)]
    v_board = [[-1] * (n+2) for _ in range(n+1)]
    t_board = [[False] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            x = i + 1
            y = j + 1
            if new_board[x][y] == 0:
                if new_board[x][y+1] == 0:
                    h_board[x][y] = 0

                if new_board[x+1][y] == 0:
                    v_board[x][y] = 0

                if new_board[x][y+1] == 0 and new_board[x+1][y] == 0 and new_board[x+1][y+1] == 0:
                    t_board[x][y] = True

    h_board[1][1] = 1
    queue = [(True, 1, 1)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while len(queue) != 0:
        horizontal, x, y = queue.pop(0)
        if horizontal:
            cur_board = h_board
            turn_board = v_board
            dtx = -1
            dty = 0
            dnx = 0
            dny = 1
            cur = True
            turn = False
        else:
            cur_board = v_board
            turn_board = h_board
            dtx = 0
            dty = -1
            dnx = 1
            dny = 0
            cur = False
            turn = True
        time = cur_board[x][y]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if cur_board[new_x][new_y] == 0:
                cur_board[new_x][new_y] = time + 1
                queue.append((cur, new_x, new_y))

        tx = x + dtx
        ty = y + dty
        if t_board[tx][ty]:
            nx = tx + dnx
            ny = ty + dny
            if turn_board[tx][ty] == 0:
                turn_board[tx][ty] = time + 1
                queue.append((turn, tx, ty))
            if turn_board[nx][ny] == 0:
                turn_board[nx][ny] = time + 1
                queue.append((turn, nx, ny))

        if t_board[x][y]:
            nx = x + dnx
            ny = y + dny
            if turn_board[x][y] == 0:
                turn_board[x][y] = time + 1
                queue.append((turn, x, y))
            if turn_board[nx][ny] == 0:
                turn_board[nx][ny] = time + 1
                queue.append((turn, nx, ny))

    if h_board[n][n-1] == -1:
        return v_board[n-1][n] - 1
    elif v_board[n-1][n] == -1:
        return h_board[n][n-1] - 1
    else:
        return min((h_board[n][n-1], v_board[n-1][n])) - 1
