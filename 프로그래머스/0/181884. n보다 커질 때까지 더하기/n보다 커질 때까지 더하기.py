def solution(numbers, n):
    answer = 0
    result = 0
    for i in numbers:
        result += i
        if result > n:
            answer = result
            break
    return answer
