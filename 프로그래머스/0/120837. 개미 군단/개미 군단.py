def solution(hp):
    answer = 0

    if hp == hp//5 * 5 :
        answer = hp // 5
    elif hp == hp//5 * 5 + hp%5//3 * 3 :
        answer = hp//5 + hp%5//3
    elif hp == hp//5 * 5 + hp%5//3 * 3 + hp%5%3//1 * 1 :
        answer = hp//5 + hp%5//3 + hp%5%3//1
        
    return answer
