def solution(numbers):
    sorted_numbers = sorted(numbers,key=None,reverse=True)
    answer = sorted_numbers[0]*sorted_numbers[1]
    return answer