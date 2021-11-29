def solution(skill, skill_tree):
    cnt = 0
    for skills in skill_tree:
        answer = ''
        for s in skills:
            if s in skill:
                answer += s
        if answer == skill[:len(answer)]:
            cnt += 1
    return cnt
