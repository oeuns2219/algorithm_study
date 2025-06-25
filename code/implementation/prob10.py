def hor(x, y, frame):
    return [x, y-1, 0] in frame or [x+1, y-1, 0] in frame or ([x-1, y, 1] in frame and [x+1, y, 1] in frame)

def ver(x, y, frame):
    return y == 0 or [x-1, y, 1] in frame or [x, y, 1] in frame or [x, y-1, 0] in frame

def solution(n, build_frame):
    frame = []

    for i in build_frame:
        x = i[0]
        y = i[1]
        if i[3]: #create
            if i[2]:
                if hor(x, y, frame):
                    frame.append([x, y, 1])
            else:
                if ver(x, y, frame):
                    frame.append([x, y, 0])

        else: #destroy
            if i[2]:
                frame.remove([x, y, 1])
                if not((not [x-1, y, 1] in frame or hor(x-1, y, frame)) and  (not [x+1, y, 1] in frame or hor(x+1, y, frame)) and (not [x, y, 0] in frame or ver(x, y, frame)) and (not [x+1, y, 0] in frame or ver(x+1, y, frame))):
                    frame.append([x, y, 1])
            else:
                frame.remove([x, y, 0])
                if not ((not [x-1, y+1, 1] in frame or hor(x-1, y+1, frame)) and (not [x, y+1, 1] in frame or hor(x, y+1, frame)) and (not [x, y+1, 0] in frame or ver(x, y+1, frame))):
                    frame.append([x, y, 0])

    frame.sort()
    return frame

