
ops = ['*', '/', '+', '-']

N = int(input())
postorder = input()
stack = []
assign = dict()
for i in range(len(postorder)):
    elem = postorder[i]
    if elem in ops:
        c = elem.join(stack[-2:])
        stack.pop()
        stack.pop()
        stack.append(str(eval(c)))
    else:
        if not elem in assign:
            val = input()
            assign[elem] = val
        stack.append(assign[elem])
res = float(stack.pop())
print('%.2f' % res)