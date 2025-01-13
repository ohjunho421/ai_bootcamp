def solution(arr1, arr2):
    anwser = 0
    l = len(arr1)
    r = len(arr2)
    if l > r : 
        answer = 1
    elif l < r : 
        answer = -1
    elif l==r : 
        if sum(arr1)>sum(arr2):
            answer = 1
        elif sum(arr1)<sum(arr2): 
            answer = -1
        else : 
            answer = 0

    return answer