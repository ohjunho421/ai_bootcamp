def solution(numbers, n):
    result = 0
    for i in numbers:
        result += i
        if n<result:
            break
    return result