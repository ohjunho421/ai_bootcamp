def solution(num1, num2):
    if not (-50000 <= num1 <= 50000):
        return -1
    if not (-50000 <= num2 <= 50000):
        return -1    
    
    answer = num1 - num2
    return answer