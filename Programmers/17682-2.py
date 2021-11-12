def solution(dartResult):
    num = []
    dartResult = dartResult.replace('10', 't')
    print(dartResult)
    key = {'S':1, 'D':2, 'T':3}
    for i in range(len(dartResult)):
        x = dartResult[i]
        if x == 't':
            num.append(10)
        elif x.isdigit():
            num.append(int(x))
        elif x in ['S', 'D', 'T']:
            num[-1] = num[-1] ** key[x]
        else:
            if x == '*':
                num[-1] *= 2
                if len(num) > 1:
                    num[-2] *= 2
            else:
                num[-1] *= -1
    return sum(num)
