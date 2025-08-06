def binary_search(lst, prefix, start, end, leftmost):
    if start > end:
        return -1
    mid = (start + end) // 2
    k = lst[mid]
    if k.startswith(prefix):
        if leftmost:
            if mid == 0 or not lst[mid - 1].startswith(prefix):
                return mid
            else:
                return binary_search(lst, prefix, start, mid - 1, leftmost)
        else:
            if mid == len(lst) - 1 or not lst[mid + 1].startswith(prefix):
                return mid
            else:
                return binary_search(lst, prefix, mid + 1, end, leftmost)
    elif k > prefix:
        return binary_search(lst, prefix, start, mid - 1, leftmost)
    else:
        return binary_search(lst, prefix, mid + 1, end, leftmost)


def solution(words, queries):
    answer = []
    k = len(words)
    rwords = [e[::-1] for e in words]
    words.sort()
    lengths = [len(e) for e in words]
    rwords.sort()
    rlengths = [len(e) for e in rwords]
    for query in queries:
        n = len(query)
        idx = query.index('?')
        pre = True
        if idx == 0:
            idx = query.rindex('?')
            pre = False
            fix = query[idx + 1:][::-1]
        else:
            fix = query[:idx]
        if pre:
            left_idx = binary_search(words, fix, 0, k - 1, True)
            if left_idx == -1:
                answer.append(0)
            else:
                right_idx = binary_search(words, fix, left_idx, k - 1, False)
                answer.append(lengths[left_idx:right_idx + 1].count(n))
        else:
            left_idx = binary_search(rwords, fix, 0, k - 1, True)
            if left_idx == -1:
                answer.append(0)
            else:
                right_idx = binary_search(rwords, fix, left_idx, k - 1, False)
                answer.append(rlengths[left_idx:right_idx + 1].count(n))
    return answer