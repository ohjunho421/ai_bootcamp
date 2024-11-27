import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    # 두 분모의 최소공배수 계산
    common_lcm = lcm(denom1, denom2)
    
    # 분자 계산: 공통 분모에 맞춰 분수를 변환한 후 더하기
    new_numer = numer1 * (common_lcm // denom1) + numer2 * (common_lcm // denom2)
    new_denom = common_lcm
    
    # 최대공약수를 구해 기약분수로 변환
    gcd = math.gcd(new_numer, new_denom)
    simplified_numer = new_numer // gcd
    simplified_denom = new_denom // gcd
    
    return [simplified_numer, simplified_denom]
