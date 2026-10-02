#제곱 개수 배열

def solution(arr, l, r):
    k = 0
    pre = 0
    a = [0, 0]
    b = [0, 0]
    for i in range(len(arr)):
        if pre + arr[i] < l:
            pre += arr[i]
        else:
            a[0] = i
            a[1] = l - pre
            break

    for i in range(a[0], len(arr)):
        if pre + arr[i] < r:
            pre += arr[i]
        else:
            b[0] = i
            b[1] = r - pre
            break

    if a[0] == b[0]:
        k = (b[1] - a[1] + 1) * arr[a[0]]
    else:
        k = (arr[a[0]] - a[1] + 1) * arr[a[0]] + b[1] * arr[b[0]]
        for i in range(a[0] + 1, b[0]):
            k += arr[i] ** 2

    c = 1
    cur_total = k
    ca, cb = a.copy(), b.copy()
    if ca[1] == 1:
        ca[0] -= 1
        if ca[0] >= 0:
            ca[1] = arr[ca[0]]
    else:
        ca[1] -= 1
    while ca[0] >= 0:
        if ca[1] <= cb[1]:
            if arr[ca[0]] == arr[cb[0]]:
                new_total = cur_total
                if new_total == k:
                    c += ca[1]

            else:
                new_total = cur_total + ca[1] * (arr[ca[0]] - arr[cb[0]])
                if (new_total >= k > cur_total or new_total <= k < cur_total) and abs(k - cur_total) % abs(arr[ca[0]] - arr[cb[0]]) == 0:
                    c += 1

            if cb[1] == ca[1]:
                cb[0] -= 1
                cb[1] = arr[cb[0]]
            else:
                cb[1] -= ca[1]
            ca[0] -= 1
            if ca[0] >= 0:
                ca[1] = arr[ca[0]]
        else:
            if arr[ca[0]] == arr[cb[0]]:
                new_total = cur_total
                if new_total == k:
                    c += cb[1]

            else:
                new_total = cur_total + cb[1] * (arr[ca[0]] - arr[cb[0]])
                if (new_total >= k > cur_total or new_total <= k < cur_total) and abs(k - cur_total) % abs(arr[ca[0]] - arr[cb[0]]) == 0:
                    c += 1

            ca[1] -= cb[1]
            cb[0] -= 1
            cb[1] = arr[cb[0]]
        cur_total = new_total

    cur_total = k
    ca, cb = a.copy(), b.copy()
    if cb[1] == arr[cb[0]]:
        cb[0] += 1
        cb[1] = 1
    else:
        cb[1] += 1
    while cb[0] < len(arr):
        left_num = arr[ca[0]] - ca[1] + 1
        right_num = arr[cb[0]] - cb[1] + 1
        if left_num <= right_num:
            if arr[ca[0]] == arr[cb[0]]:
                new_total = cur_total
                if new_total == k:
                    c += left_num

            else:
                new_total = cur_total + left_num * (arr[cb[0]] - arr[ca[0]])
                if (new_total >= k > cur_total or new_total <= k < cur_total) and abs(k - cur_total) % abs(arr[cb[0]] - arr[ca[0]]) == 0:
                    c += 1
            ca[0] += 1
            ca[1] = 1
            if left_num == right_num:
                cb[0] += 1
                cb[1] = 1
            else:
                cb[1] += left_num
        else:
            if arr[ca[0]] == arr[cb[0]]:
                new_total = cur_total
                if new_total == k:
                    c += right_num

            else:
                new_total = cur_total + right_num * (arr[cb[0]] - arr[ca[0]])
                if (new_total >= k > cur_total or new_total <= k < cur_total) and abs(k - cur_total) % abs(arr[cb[0]] - arr[ca[0]]) == 0:
                    c += 1
            ca[1] += right_num
            cb[0] += 1
            cb[1] = 1
        cur_total = new_total

    return [k, c]

