def solution(s1, s2):
    a = set(s1) & set(s2)
    answer = len(list(a))
    return answer