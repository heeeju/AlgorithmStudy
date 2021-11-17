def solution(arr):
    def gcd(x,y): #from math import gcd 사용가능
        while y:
            x, y = y, x % y
        return x

    def lcm(x,y):
        return x * y // gcd(x,y)

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]
