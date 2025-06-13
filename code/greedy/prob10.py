#baekjoon prob no.2839
n = int(input())
num = n // 5
rest = n % 5

def count_bag(n, r):
    while n != -1:
        if r % 3 == 0:
            return n + (r // 3)
        else:
            n -= 1
            r += 5
    return -1

print(count_bag(num, rest))