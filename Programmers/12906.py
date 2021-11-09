def solution(arr):
    answer = []
    arr.append(-1)
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i-1])
    return answer
