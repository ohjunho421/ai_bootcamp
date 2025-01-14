def solution(numbers):
    numbers.sort()
    max1=numbers[0] * numbers[1]
    max2=numbers[-1] * numbers[-2]
    
    return max(max1,max2)
    