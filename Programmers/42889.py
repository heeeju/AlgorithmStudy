import collections

def solution(N, stages):
    userCount = collections.Counter(stages)
    info = {}
    user = userCount[N+1]
    for i in range(N, 0, -1):
        user += userCount[i]
        if user == 0:
            info[i] = 0
        else:
            info[i] = userCount[i] / user
    info = sorted(info.items(), key = lambda x : (-x[1], x[0]))

    return [i[0] for i in info]
