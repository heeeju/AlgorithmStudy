def solution(progresses, speeds):
    answer = []
    days = []
    for p, s in zip(progresses, speeds):
        day = (100-p)//s if (100-p)/s % 1 ==0 else (100-p)//s+1
        if len(days)==0 or days[-1] < day:
            answer.append(1)
            days.append(day)
        else:
            answer[-1] += 1
    return answer
