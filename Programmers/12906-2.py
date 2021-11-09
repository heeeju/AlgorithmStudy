def solution(arr):
    answer = []
    for x in arr:
        if answer[-1:] == [x]:
        #if answer[-1] == x 이렇게 적으면 index 오류
            continue
        answer.append(x)
    return answer
