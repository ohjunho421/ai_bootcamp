def solution(num_list):
    
    mul_number = 1
    for i in num_list:
        mul_number *= i    
    
    add_number = sum(num_list)**2
    
    if mul_number > add_number :
        answer = 0
    elif mul_number < add_number :
        answer = 1
        
    return answer