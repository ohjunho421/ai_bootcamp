def solution(numbers):
    # map을 사용해 각 값을 2배로 처리
    answer = list(map(lambda x: x * 2, numbers))
    return answer
