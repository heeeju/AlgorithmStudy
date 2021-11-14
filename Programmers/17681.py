def solution(n, arr1, arr2):
    info = []
    key = {1:'#', 0:' '}
    for i in range(n):
        num = arr1[i]
        num2 = arr2[i]
        map = []
        while len(map)!= n:
            map += [key[num%2 or num2%2]]
            num //= 2
            num2 //= 2
        map.reverse()
        info.append(map)
    answer = []
    for i in info:
        answer.append(''.join(i))

    return answer
