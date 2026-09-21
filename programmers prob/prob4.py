#당구 연습
#float 연산 오류 주의

def solution(m, n, startX, startY, balls):
    answer = []

    for endX, endY in balls:
        if startX == endX:
            a = abs(startY - endY) / 2
            b = min(startX, m - startX)
            c_square = a ** 2 + b ** 2
            if startY < endY:
                c = startY + endY
            else:
                c = 2 * n - startY - endY
            answer.append(min(c_square * 4, c ** 2))
        elif startY == endY:
            a = abs(startX - endX) / 2
            b = min(startY, n - startY)
            c_square = a ** 2 + b ** 2
            if startX < endX:
                c = startX + endX
            else:
                c = 2 * m - startX - endX
            answer.append(min(c_square * 4, c ** 2))
        else:
            lst = []
            a = 2 * n - startY - endY
            b = abs(startX - endX)
            c_square = a ** 2 + b ** 2
            lst.append(c_square)

            a = startY + endY
            b = abs(startX - endX)
            c_square = a ** 2 + b ** 2
            lst.append(c_square)

            a = 2 * m - startX - endX
            b = abs(startY - endY)
            c_square = a ** 2 + b ** 2
            lst.append(c_square)

            a = startX + endX
            b = abs(startY - endY)
            c_square = a ** 2 + b ** 2
            lst.append(c_square)

            answer.append(min(lst))

    return answer

print(solution(10,	10,	3,	7,	[[7, 7], [2, 7], [7, 3]]))