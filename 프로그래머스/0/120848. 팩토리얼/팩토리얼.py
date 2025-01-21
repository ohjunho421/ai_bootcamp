def solution(n):
    x = 1
    fact = 1
    while fact *(x+1) <= n:
        x += 1
        fact *= x
        
    return x