def solution(s):
    num = len(s)//2
    if len(s) % 2 == 0:
        return s[num-1:num+1]
    return s[num-1:num+1]
