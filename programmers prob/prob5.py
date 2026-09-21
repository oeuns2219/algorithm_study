#유사 칸토어 비트열

def solution(n, l, r):
    answer = 0
    total = 5 ** (n)
    block = 5 ** (n - 1)
    start = l

    if l == 1 and r == total:
        return 4 ** (n)

    for i in range(1, 6):
        if start <= i * block:
            if i == 3:
                if r <= i * block:
                    break
                else:
                    start = i * block + 1
                    continue

            ignore = (i - 1) * block
            if r <= i * block:
                answer += solution(n - 1, start - ignore, r - ignore)
                break
            else:
                answer += solution(n - 1, start - ignore, block)
                start = i * block + 1

    return answer