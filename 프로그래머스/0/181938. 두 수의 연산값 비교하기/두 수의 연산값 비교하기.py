def solution(a, b):
    lista=[str(a)]
    listb=[str(b)]
    listab=lista + listb

    ab="".join(listab)
    ab=int(ab)
    
    if ab < 2*a*b :
        return 2*a*b
    else : 
        return ab
    return 