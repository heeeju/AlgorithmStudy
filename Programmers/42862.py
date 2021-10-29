def solution(n, lost, reserve):
    student = [1 for i in range(0,n+2)]
    for l in lost:
        student[l] -= 1
    for r in reserve:
        student[r] += 1
    for i in range(1,n+1):
        if student[i]==2:
            student[i] -= 1
            if student[i-1] == 0:
                student[i-1] += 1
            elif student[i+1] == 0:
                student[i+1] += 1
    answer = sum(student[1:-1])
    return answer
