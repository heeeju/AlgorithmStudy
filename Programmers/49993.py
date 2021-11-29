def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        idx = 0
        flag = 0
        for s in skills:
            if s in skill:
                if skill[idx] == s:
                    idx += 1
                else:
                    flag = 1
                    break;
        if flag == 0:
            answer += 1
    return answer
