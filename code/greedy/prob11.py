n = int(input())
start_lst = []
end_lst = []
for _ in range(n):
    s, e = map(int, input().split())
    start_lst.append(s)
    end_lst.append(e)

start_lst = [t for _, t in sorted(zip(end_lst, start_lst))]
end_lst.sort()

cnt = 0
cur = 0
for i in range(n):
    if start_lst[i] >= cur:
        cur = end_lst[i]
        cnt += 1

print(cnt)