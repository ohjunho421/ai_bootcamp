def solution(my_string):
    answer = 0
    number = ([int(char) for char in my_string if char.isdigit()])
    answer = sum(number)
    return answer