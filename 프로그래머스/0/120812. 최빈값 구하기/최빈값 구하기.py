def solution(array):
    freq = {}
    for i in array:
        if i in freq:  
            freq[i] += 1
        else:
            freq[i] = 1

    max_count = max(freq.values()) 
    modes = [key for key, count in freq.items() if count == max_count]

    if len(modes) > 1:
        return -1

    return modes[0]  
