def operate(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        if a < 0:
            return -((-a) // b)
        else:
            return a // b

def calculate_all(nums, ops):
    global results
    if ops.count(0) == 4:
        results.append(nums[0])

    else:
        for i in range(4):
            if ops[i] != 0:
                new_nums = nums.copy()
                new_ops = ops.copy()
                new_ops[i] -= 1
                a = new_nums.pop(0)
                b = new_nums[0]
                new_nums[0] = operate(a, b, i)
                calculate_all(new_nums, new_ops)

n = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))
results =[]

calculate_all(numbers, operations)
print(max(results))
print(min(results))