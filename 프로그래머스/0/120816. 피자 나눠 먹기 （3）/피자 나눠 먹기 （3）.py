def solution(slice, n):
    answer = n//slice
    if n%slice == 0 :
        answer = n//slice
    else :
        answer = n//slice +1
    return answer