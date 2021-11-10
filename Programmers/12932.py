def solution(n):
    return [int(x) for x in (str(n))][::-1]
    #return list(map(int, reversed(str(n))))
