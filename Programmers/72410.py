def solution(new_id):
    answer = ''
    usable = ['-', '_', '.']
    for ch in new_id:
        if ch.isalpha():
            if ch.isupper():
                answer += ch.lower()
            else:
                answer += ch
        elif ch.isdigit():
            answer += ch
        elif ch in usable:
            answer += ch
    while answer.find('..') != -1:
        answer = answer.replace('..', '.')
    while len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    while len(answer) > 0 and answer[len(answer)-1] == '.':
        answer = answer[:len(answer)-1]
    if len(answer) == 0:
        answer+= 'a'
    if len(answer) >= 16:
        answer = answer[:15]
    while len(answer) > 0 and answer[len(answer)-1] == '.':
        answer = answer[:len(answer)-1]
    while len(answer) <= 2:
        answer += answer[len(answer)-1]

    return answer
