#아날로그 시계

def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    answer = 0

    cur = start * 719
    if cur % 43200 != 0:
        cur += 43200 - (cur % 43200)
    while cur <= end * 719:
        answer += 1
        if (cur / 719 * 708) % 43200 == 0:
            answer -= 1
        cur += 43200
    cur = start * 708
    if cur % 43200 != 0:
        cur += 43200 - (cur % 43200)
    while cur <= end * 708:
        answer += 1
        cur += 43200

    return answer