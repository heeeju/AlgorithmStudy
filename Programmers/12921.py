import math

def solution(n):
    answer = [2] #1은 소수가 아니고, 2는 소수이다
    for i in range(3, n+1): #3부터 비교
        check = 0
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                check = 1
                break;
        if not check:
            answer += [i]

    return len(answer)

'''
# 참고하면 좋을 코드
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''
