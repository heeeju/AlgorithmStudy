def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = [i]
        for j in range(1, i//2+1):
            if i % j == 0:
                count.append(j)
        if len(count) % 2 == 0 :
            answer += i
        else:
            answer -= i
    return answer
