def solution(rsp):
    win = {'2':'0','0':'5','5':'2'}
    
    answer = ''.join([win[char] for char in str(rsp)])
    return answer