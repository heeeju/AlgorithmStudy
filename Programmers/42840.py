def solution(answers):
    p1 = [x%5+1 for x in range(len(answers))]
    pattern = [2,1,2,3,2,4,2,5]
    p2 = [pattern[i%8] for i in range(len(answers))]
    pattern = [3,1,2,4,5]
    p3 = [pattern[(i)//2%5] for i in range(len(answers))]

    c1 = [1 for i in range(len(answers)) if answers[i]==p1[i]]
    c2 = [1 for i in range(len(answers)) if answers[i]==p2[i]]
    c3 = [1 for i in range(len(answers)) if answers[i]==p3[i]]

    answer = []
    max_cnt = max(sum(c1),sum(c2),sum(c3))
    if sum(c1) == max_cnt:
        answer.append(1)
    if sum(c2) == max_cnt:
        answer.append(2)
    if sum(c3) == max_cnt:
        answer.append(3)
    return answer
