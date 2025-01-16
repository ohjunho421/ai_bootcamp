def create_dict():
    key = range(10)
    value = [chr(i) for i in range(ord('a'), ord('j') + 1)]
    return dict(zip(key, value))

def solution(age):
    answer = ''
    p_age = list(map(int, str(age)))
    mapping_dict = create_dict() 

    for digit in p_age:
        answer += mapping_dict[digit]  
    return answer
