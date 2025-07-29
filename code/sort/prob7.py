n = int(input())
decks = []
for _ in range(n):
    decks.append(int(input()))

cnt = 0
while len(decks) > 1:
    decks.sort()
    a = decks.pop(0)
    b = decks.pop(0)
    c = a + b
    cnt += c
    decks.append(c)
print(cnt)