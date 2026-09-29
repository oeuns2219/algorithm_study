#숫자 야구

from itertools import permutations

def lst_to_int(lst):
    res = 0
    for i in range(4):
        res += lst[i] * 10 ** (3 - i)
    return res

def submit2(answer, guess):
    set1 = set()
    set2 = set()
    s_num = 0
    for i in range(4):
        i1, i2 = (answer // 10 ** i) % 10, (guess // 10 ** i) % 10
        if i1 == i2:
            s_num += 1
        set1.add(i1)
        set2.add(i2)
    num = len(set1.intersection(set2))
    return str(s_num) + 'S ' + str(num - s_num) + 'B'

def solution(n, submit):
    answer = 0
    cases = list(range(1, 10))
    all_case = list(permutations(cases, 4))
    res1 = submit(1234)
    pos_case = []

    if res1 == '4S 0B':
        return 1234

    for case in all_case:
        ans = lst_to_int(case)
        if res1 == submit2(ans, 1234):
            pos_case.append(case)

    pass_case = []
    while len(pos_case) > 1:
        guess = pos_case[0]
        num = lst_to_int(guess)
        res = submit(num)
        if res == '4S 0B':
            answer = num
            break
        for case in pos_case:
            ans = lst_to_int(case)
            if res == submit2(ans, num):
                pass_case.append(case)
        pos_case = pass_case
        pass_case = []
    if answer == 0:
        answer = lst_to_int(pos_case[0])
    return answer