N = int(input())

res = 1

while N % 2 == 0:
    N //= 2
    res *= 2

cards = list(range(1, N + 1))
while len(cards) != 1:
    new_cards = []
    if len(cards) % 2 != 0:
        new_cards.append(cards.pop())
    cards = new_cards + cards[1::2]
print(res * cards[0])