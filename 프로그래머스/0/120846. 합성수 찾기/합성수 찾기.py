def solution(n):
    count_numbers = 0
    for i in range(1,n+1) :
        count = 0
        for j in range(1, int(i**0.5)+1):
           if i % j == 0:
                count += 1
                if j != i // j:
                    count += 1
                    
        if count >= 3 :
            count_numbers += 1
            
    return count_numbers