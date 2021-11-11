def solution(s, n):
    info = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    info_l = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
    answer = ""
    for ch in s:
        if ch.isupper():
            answer += info[(info.index(ch)+n) % 26]
        elif ch.islower():
            answer += info_l[(info_l.index(ch)+n) % 26]
        else:
            answer += ch
    return answer
    #list 대신 ord 사용가능!
