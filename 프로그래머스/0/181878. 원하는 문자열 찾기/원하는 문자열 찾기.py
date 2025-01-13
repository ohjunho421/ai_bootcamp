def solution(myString, pat):
    answer = 0
    m = myString.lower()
    p = pat.lower()
    answer = 1 if m.find(p) != -1 else 0
    
    return answer