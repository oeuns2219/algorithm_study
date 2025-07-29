n = int(input())
lst = []
for _ in range(n):
    input_data = input().split()
    lst.append((-int(input_data[1]), int(input_data[2]), -int(input_data[3]), input_data[0]))
lst.sort()
for _, _, _, name in lst:
    print(name)