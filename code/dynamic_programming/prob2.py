n = int(input())
food_lst = list(map(int, input().split()))
memo_lst = [0] * n

memo_lst[0] = food_lst[0]
memo_lst[1] = max(food_lst[:2])
memo_lst[2] = max((food_lst[0] + food_lst[2], food_lst[1]))
for i in range(3, n):
    memo_lst[i] = max((food_lst[i] + memo_lst[i - 2], food_lst[i - 1] + memo_lst[i - 3]))

print(memo_lst)
print(memo_lst[n-1])