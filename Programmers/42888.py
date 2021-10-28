def solution(record):
    answer = []
    dic = {}

    for command in record:
        command = command.split()
        if command[0] == 'Enter':
            dic[command[1]] = command[2]
        elif command[0] == 'Change':
            dic[command[1]] = command[2]

    for command in record:
        command = command.split()
        if command[0] == 'Enter':
            answer.append(dic[command[1]]+'님이 들어왔습니다.')
        elif command[0] == 'Leave':
            answer.append(dic[command[1]]+'님이 나갔습니다.')

    return answer
