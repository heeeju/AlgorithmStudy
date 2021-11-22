def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = lambda x : (x*4)[:4], reverse = True)
    return str(int(''.join(numbers)))
    #return ''.join(numbers) => X
    # 반례 [0,0,0,0]
    # 기대값 : "0"
    # 결과값 : "0000"
