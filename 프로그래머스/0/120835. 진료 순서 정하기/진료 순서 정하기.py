def solution(emergency):
    sorted_emergency = sorted(emergency, reverse = True)
    answer = [sorted_emergency.index(num) + 1 for num in emergency]
    
    
    return answer