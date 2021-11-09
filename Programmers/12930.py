def solution(s):
    answer = ""
    idx = 0
    for ch in s:
        if idx % 2 == 0 :
            answer+= ch.upper()
        else :
            answer += ch.lower()
        if ch == ' ':
            idx = 0
        else:
            idx += 1
    return answer
