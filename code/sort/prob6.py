def solution(N, stages):
    f_lst = []
    for i in range(1, N+1):
        arrived = [e for e in stages if e >= i]
        blocked = stages.count(i)
        if len(arrived) == 0:
            fail_rate = 0
        else:
            fail_rate = blocked / len(arrived)
        f_lst.append((fail_rate, i))
    f_lst.sort(key=lambda x: (-x[0], x[1]))
    res = [stage for _, stage in f_lst]
    return res