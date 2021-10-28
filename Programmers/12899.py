def solution(n):
    dic = {1:'1', 2:'2', 0:'4'}
    answer = ''
    while n > 0:
        answer+= dic[n%3]
        if n%3 == 0:
            n -= 1
        n //= 3
    return answer[::-1]
