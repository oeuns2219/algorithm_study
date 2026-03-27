
priority = {'*': 1, '/': 1, '+': 0, '-': 0}

inorder = input()
postorder = []
env_pri = 0
stack = []
for i in range(len(inorder)):
    elem = inorder[i]
    if elem in priority:
        elem_pri = env_pri + priority[elem]
        if len(stack) == 0:
            stack.append((elem, elem_pri))
        else:
            while stack:
                if elem_pri > stack[-1][1]:
                    break
                else:
                    old, _ = stack.pop()
                    postorder.append(old)
            stack.append((elem, elem_pri))
    elif elem == '(':
        env_pri += 2
    elif elem == ')':
        env_pri -= 2
    else:
        postorder.append(elem)
while stack:
    elem, _ = stack.pop()
    postorder.append(elem)
print(''.join(postorder))