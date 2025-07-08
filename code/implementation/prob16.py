front = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def clean_room(room_map, row, column, direction, count):
    global front
    if room_map[row][column] == 0:
        count += 1
        room_map[row][column] = 2

    if room_map[row + front[0][0]][column + front[0][1]] == 0 or room_map[row + front[1][0]][column + front[1][1]] == 0 or room_map[row + front[2][0]][column + front[2][1]] == 0 or room_map[row + front[3][0]][column + front[3][1]] == 0:
        direction -= 1
        if direction == -1: direction = 3
        front_row = row + front[direction][0]
        front_column = column + front[direction][1]
        if room_map[front_row][front_column] == 0:
            return clean_room(room_map, front_row, front_column, direction, count)
        else:
            return clean_room(room_map, row, column, direction, count)
    else:
        back_row = row - front[direction][0]
        back_column = column - front[direction][1]
        if room_map[back_row][back_column] != 1:
            return clean_room(room_map, back_row, back_column, direction, count)
        else:
            return count

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))
print(clean_room(room, r, c, d, 0))
