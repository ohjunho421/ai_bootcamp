def solution(num_list):
    even_number = [x/2 for x in num_list if x%2 == 0]
    odd_number = [x/2 for x in num_list if x%2 != 0]
    answer = [len(even_number),len(odd_number)]
    return answer