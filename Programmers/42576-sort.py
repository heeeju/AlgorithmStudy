def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
'''
시간초과
def solution(participant, completion):
    answer = participant
    for c in completion:
        answer.remove(c)
    return answer[0]
'''
