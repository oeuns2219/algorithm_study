n = int(input())
one_hour = 45 * 15 + 15 * 60
third_hour = 60 * 60
q = n // 3
r = n % 3 + 1

print(q * third_hour + (q * 2 + r) * one_hour)