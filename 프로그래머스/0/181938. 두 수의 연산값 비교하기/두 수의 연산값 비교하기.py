def solution(a, b):
    answer = 0
    lista = []
    lista.append(str(a))
    lista.append(str(b))

    addlist = int(''.join(lista))
    if addlist > 2*a*b :
        answer = addlist
    else :
        answer = 2*a*b
        
    return answer