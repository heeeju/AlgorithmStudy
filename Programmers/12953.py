def solution(arr):
    while True:
        n = arr.pop()
        if len(arr) == 0:
            return n
        m = arr.pop()
        div_n = [n]
        div_m = [m]
        for i in range(1,n//2+1):
            if n % i == 0:
                div_n.append(i)
        for i in range(1,m//2+1):
            if m % i == 0:
                div_m.append(i)
        divisor = max(list(set(div_n) & set(div_m)))
        arr.append(n * m // divisor)
