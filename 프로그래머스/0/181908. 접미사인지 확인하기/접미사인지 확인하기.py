def solution(my_string, is_suffix):
    if len(my_string) < len(is_suffix):
        answer = 0
    elif len(my_string) >= len(is_suffix):
        answer = 1 if my_string.endswith(is_suffix) else 0

    return answer 