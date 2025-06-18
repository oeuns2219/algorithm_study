pos = input()

if pos[0] in 'cdef' and pos[1] in '3456': print(8)
elif (pos[0] in 'cdef' and pos[1] in '27') or (pos[0] in 'bg' and pos[1] in '3456'): print(6)
elif (pos[0] in 'cdef' and pos[1] in '18') or (pos[0] in 'ah' and pos[1] in '3456') or (pos[0] in 'bg' and pos[1] in '27'): print(4)
elif (pos[0] in 'ah' and pos[1] in '27') or (pos[0] in 'bg' and pos[1] in '18'): print(3)
else: print(2)