def no_zero(lck):
    for lst in lck:
        for e in lst:
            if e == 0:
                return False
    return True

def rotate90(key):
    m = len(key)
    new_key = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new_key[j][m-i-1] = key[i][j]
    return new_key

def key_test(key, lock):
    m = len(key)
    n = len(lock)
    k = n + m - 1
    fail_flag = False
    success_flag = False

    for i in range(k):
        for j in range(k):
            copy_lock = [elem[:] for elem in lock]
            for a in range(m):
                for b in range(m):
                    x = i - m + 1 + a
                    y = j - m + 1 + b
                    if x < 0 or y < 0 or x >= n or y >= n:
                        continue
                    else:
                        copy_lock[x][y] += key[a][b]
                        if copy_lock[x][y] == 0 or copy_lock[x][y] == 2:
                            fail_flag = True
                            break
                if fail_flag:
                    break
            if fail_flag:
                fail_flag = False
                continue
            else:
                if no_zero(copy_lock):
                    success_flag = True
                    break
        if success_flag:
            break
    return success_flag

def solution(key, lock):
    key2 = rotate90(key)
    key3 = rotate90(key2)
    key4 = rotate90(key3)

    return key_test(key, lock) or key_test(key2, lock) or key_test(key3, lock) or key_test(key4, lock)

print(solution([[0,0,0],[1,0,0],[0,1,1]], [[1,1,1],[1,1,0],[1,0,1]]))