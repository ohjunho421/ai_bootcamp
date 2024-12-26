def solution(a, b):
    ab = int(''.join(map(str,[a,b])))
    ba = int(''.join(map(str,[b,a])))
    if ab > ba:
        return ab
    else :
        return ba
    