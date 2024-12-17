def solution(sides):
    sides.sort()
    sides_tuple = tuple(sides)
        
    longest= sides_tuple[-1]
    others = sum(sides_tuple[:-1])
    
    if longest < others :
        return 1
    else :
        return 2
    return answer