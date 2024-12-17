def solution(n):
    answer = 0
    if n%2 == 0:
        for j in range(2,n+1,2):
            answer += j**2
    else : 
        for i in range(1,n+1,2):
            answer += i
    return answer