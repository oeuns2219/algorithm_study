n = int(input())
town = list(map(int, input().split()))
town.sort()

print(town[(n - 1)//2])