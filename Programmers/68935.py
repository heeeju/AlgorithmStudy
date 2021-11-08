def solution(n):
    answer = 0
    str_n = ""
    while n > 0:
        str_n += str(n%3)
        n //= 3
    for i in range(len(str_n)):
        #answer += 3**i * int(str_n[len(str_n)-i-1])
        answer = int(str_n, 3)

    return answer
