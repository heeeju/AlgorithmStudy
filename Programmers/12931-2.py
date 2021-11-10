def add(n):
    if n < 10:
        return n
    return n % 10 + add(n//10)

def solution(n):
    return add(n)
