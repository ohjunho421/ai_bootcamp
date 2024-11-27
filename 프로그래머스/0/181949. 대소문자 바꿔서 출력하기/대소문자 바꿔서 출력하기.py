str_input = input()  # 문자열 입력

# 조건 확인 함수
def validate_string(s):
    return 1 <= len(s) <= 20 and s.isalpha()

# 조건 확인 및 처리
if validate_string(str_input):
    # 대소문자 변환
    print(str_input.swapcase())
else:
    print("입력된 문자열이 조건을 만족하지 않습니다.")
