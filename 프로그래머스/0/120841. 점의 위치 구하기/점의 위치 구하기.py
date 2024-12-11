def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        result = 1
    elif dot[0] > 0 and dot[1] < 0:
        result = 4
    elif dot[0] < 0 and dot[1] < 0:
        result = 3
    else :
        result = 2
    answer = result
    return answer