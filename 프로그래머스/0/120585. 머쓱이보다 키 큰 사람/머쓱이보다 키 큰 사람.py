def solution(array, height):
    sorted_array = sorted(array, reverse=True)
    count = 0
    for value in sorted_array :
        if value > height :
            count += 1
        
    return count