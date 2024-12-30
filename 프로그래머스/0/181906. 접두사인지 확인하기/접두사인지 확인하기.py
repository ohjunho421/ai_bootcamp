def solution(my_string, is_prefix):
    if len(my_string) < len(is_prefix):
        answer = 0
    elif len(my_string) >= len(is_prefix):
        answer = 1 if my_string.startswith(is_prefix) else 0

    return answer 