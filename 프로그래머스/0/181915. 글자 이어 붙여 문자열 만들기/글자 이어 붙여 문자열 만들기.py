def solution(my_string, index_list):
    answer = ''
    
    a = dict(zip(range(len(my_string)),my_string))
    
    answer = ''.join([a[index] for index in index_list if index in a])
    return answer