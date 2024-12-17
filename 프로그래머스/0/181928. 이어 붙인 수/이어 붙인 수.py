def solution(num_list):
    answer = 0
    list_o=[]
    list_e=[]
    for value in num_list:
        if value%2==0:
            list_e.append(value)
        else :
            list_o.append(value)
    
    odd=int(''.join(map(str,list_o)))
    even=int(''.join(map(str,list_e)))
    
    answer = odd + even
    return answer