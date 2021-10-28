def solution(n):
    key = ['1','2','4']
    answer = ''
    while n > 0:
        n -= 1
        answer += key[n%3]
        n //= 3
    return answer[::-1]
