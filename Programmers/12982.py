def solution(d, budget):
    answer = 0
    d.sort(reverse = True)
    while len(d) > 0 and budget >= d[-1]:
        budget -= d.pop()
        answer += 1
    return answer
