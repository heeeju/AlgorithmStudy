def add(x):
    if x < 10:
        return x
    else:
        return x % 10 + add(x//10)

def solution(x):
    return x % add(x) == 0
    #return x % sum([int(i) for i in str(x)]) == 0
    #return x // add(x) == x / add(x)
