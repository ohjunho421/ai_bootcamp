import itertools

def solution(numbers, k):
    cycle = itertools.cycle(numbers)
    for _ in range(2*k-1):
        value = next(cycle)
    return value