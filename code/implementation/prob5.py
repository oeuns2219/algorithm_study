score = input()
n = len(score) // 2
left = 0
right = 0
for i in range(n):
    left += int(score[i])
    right += int(score[n + i])
if left == right: print('LUCKY')
else: print('READY')