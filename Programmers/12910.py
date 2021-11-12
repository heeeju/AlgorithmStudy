def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    return sorted(answer) if len(answer) != 0 else [-1]

    #return sorted( [x for x in arr if x % divisor == 0]) or [-1]
