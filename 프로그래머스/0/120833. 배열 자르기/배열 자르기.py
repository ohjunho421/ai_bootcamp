def solution(numbers, num1, num2):
    slice_obj = slice(num1,num2+1)
    answer = numbers[slice_obj]
    return answer