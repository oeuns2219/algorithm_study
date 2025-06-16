n = int(input())
load_len = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

cur_city = 0
next_city = 1
total_price = 0

while cur_city != n-1:
    if oil_price[cur_city] > oil_price[next_city] or next_city == n-1:
        total_price += oil_price[cur_city] * sum(load_len[cur_city:next_city])
        cur_city = next_city
    next_city += 1

print(total_price)