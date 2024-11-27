def solution(num1, num2):
    # 입력값 검증
    if not (0 <= num1 <= 100):
        return -1  # num1이 조건을 만족하지 않음
    if not (0 <= num2 <= 100):
        return -1  # num2가 조건을 만족하지 않음

    # 계산
    answer = num1 * num2  # 정수 값 할당
    return answer         # 결과 반환
