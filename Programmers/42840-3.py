def solution(answers):
    sheet = []
    answer = []
    pattern = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    count = [0,0,0]

    for idx, a in enumerate(answers):
        for i in range(3):
            if pattern[i][idx%len(pattern[i])] == a:
                count[i] += 1

    for i in range(3):
        if count[i]==max(count):
            print()
            answer += [i+1]

    return answer
