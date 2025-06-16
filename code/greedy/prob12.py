def twice_or_ten(value, target, count):
    global cnt
    count += 1
    if value == target:
        if cnt == None:
            cnt = count
        else:
            cnt = min(cnt, count)
        return True

    else:
        if target > 10 * value:
            return twice_or_ten(2 * value, target, count) or twice_or_ten((10 * value) + 1, target, count)
        elif target >= 2 * value:
            return twice_or_ten(2 * value, target, count)
        else:
            return False

a, b = map(int, input().split())
cnt = None

if twice_or_ten(a, b, 0):
    print(cnt)
else:
    print(-1)