def solution(dartResult):
    num = []
    dartResult = list(dartResult)
    key = {'S':1, 'D':2, 'T':3}
    for i in range(len(dartResult)):
        x = dartResult[i]
        if x.isdigit():
            if x == '1' and dartResult[i+1] == '0': #Index 초과 생각할 필요 X -> 어차피 뒤에 SDT 있음
                num.append(10)
                dartResult[i+1] = 'S'
            else:
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
