def solution(my_string):
    remove_char = 'aeiou'
    answer = my_string.translate(str.maketrans("","",remove_char))
    return answer