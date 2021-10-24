def solution(new_id):
    answer = ''
    usable = ['-', '_', '.']
    #1
    new_id = new_id.lower()
    #2
    for ch in new_id:
        if ch.isalpha() or ch.isdigit() or ch in usable:
            answer += ch
    #3
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]

    #5
    if len(answer) == 0:
        answer+= 'a'

    #6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    #7
    while len(answer) <= 2:
        answer += answer[-1]

    return answer
