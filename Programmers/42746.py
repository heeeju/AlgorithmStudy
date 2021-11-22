def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = lambda x : x*4, reverse = True) #x*3도 가능!
    return str(int(''.join(numbers)))
    #return ''.join(numbers) => X
    # 반례 [0,0,0,0]
    # 기대값 : "0"
    # 결과값 : "0000"
