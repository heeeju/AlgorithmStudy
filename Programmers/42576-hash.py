def solution(participant, completion):
    dic = {}
    sum = 0
    for p in participant:
        dic[hash(p)] = p
        sum += hash(p)
    for c in completion:
        sum -= hash(c)

    return dic[sum]
